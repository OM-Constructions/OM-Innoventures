import uuid
import secrets
import datetime
from typing import Optional, Union
from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.models import User
from app.schemas import (
    UserCreate,
    UserLogin,
    UserOut,
    Token,
    VerifyOtpRequest,
    ResendOtpRequest,
    SignupResponse,
)
from app.services.auth_service import hash_password, verify_password
from app.services.token_service import create_access_token, decode_access_token
from app.services.email_service import send_otp_email

router = APIRouter(prefix="/auth", tags=["auth"])


def generate_six_digit_otp() -> str:
    """Generates a secure 6-digit numeric OTP code."""
    return f"{secrets.randbelow(900000) + 100000}"


def get_current_user_optional(
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db)
) -> Optional[User]:
    if not authorization:
        return None
    try:
        scheme, token = authorization.split(" ")
        if scheme.lower() != "bearer":
            return None
        payload = decode_access_token(token)
        if not payload or "sub" not in payload:
            return None
        raw_id = payload["sub"]
        try:
            user_uuid = uuid.UUID(str(raw_id))
            return db.query(User).filter(User.id == user_uuid).first()
        except (ValueError, AttributeError):
            return db.query(User).filter(User.id == raw_id).first()
    except Exception:
        return None


def get_current_user(
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db)
) -> User:
    user = get_current_user_optional(authorization, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required. Please log in.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def get_current_admin(
    authorization: Optional[str] = Header(None),
    x_admin_key: Optional[str] = Header(None, alias="X-Admin-Key"),
    db: Session = Depends(get_db)
) -> User:
    # Check Admin Header Key
    if x_admin_key and x_admin_key == settings.ADMIN_SECRET_KEY:
        user = get_current_user_optional(authorization, db)
        if user:
            return user
        admin_user = db.query(User).filter(User.is_admin == True).first()
        if admin_user:
            return admin_user
        # Create or return system admin
        system_admin = db.query(User).filter(User.email == "admin@ominnoventures.com").first()
        if not system_admin:
            system_admin = User(
                name="System Admin",
                email="admin@ominnoventures.com",
                password_hash=hash_password(settings.ADMIN_SECRET_KEY),
                is_verified=True,
                is_admin=True
            )
            db.add(system_admin) 
            db.commit()
            db.refresh(system_admin)
        return system_admin

    # Check logged-in user is_admin flag
    user = get_current_user(authorization, db)
    if not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required."
        )
    return user


@router.post("/signup", response_model=SignupResponse, status_code=status.HTTP_200_OK)
def signup(user_in: UserCreate, db: Session = Depends(get_db)):
    email_clean = user_in.email.lower().strip()
    
    try:
        existing = db.query(User).filter(User.email == email_clean).first()
    except Exception as db_err:
        print(f"[Database Error in Signup query]: {db_err}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection error. Please verify the Supabase Connection Pooler configuration."
        )
    
    otp = generate_six_digit_otp()
    otp_hash = hash_password(otp)
    otp_expires = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)

    try:
        if existing:
            if existing.is_verified:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="An account with this email already exists."
                )
            # Existing unverified user — update credentials and refresh OTP
            existing.name = user_in.name.strip()
            existing.password_hash = hash_password(user_in.password)
            if user_in.phone:
                existing.phone = user_in.phone.strip()
            existing.otp_hash = otp_hash
            existing.otp_expires_at = otp_expires
            existing.otp_attempts = 0
            db.commit()
            db.refresh(existing)
            user_name = existing.name
        else:
            user = User(
                name=user_in.name.strip(),
                email=email_clean,
                phone=user_in.phone.strip() if user_in.phone else None,
                password_hash=hash_password(user_in.password),
                is_verified=False,
                otp_hash=otp_hash,
                otp_expires_at=otp_expires,
                otp_attempts=0,
            )
            db.add(user)
            db.commit()
            db.refresh(user)
            user_name = user.name
    except HTTPException:
        raise
    except Exception as db_err:
        print(f"[Database Error in Signup commit]: {db_err}")
        try:
            db.rollback()
        except Exception:
            pass
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Database write error: {str(db_err)}"
        )

    # Send OTP Email to client
    send_otp_email(to_email=email_clean, name=user_name, otp=otp)

    return SignupResponse(
        success=True,
        requires_otp=True,
        email=email_clean,
        message="A 6-digit verification code has been sent to your email."
    )


@router.post("/verify-otp", response_model=Token)
def verify_otp(payload: VerifyOtpRequest, db: Session = Depends(get_db)):
    email_clean = payload.email.lower().strip()
    user = db.query(User).filter(User.email == email_clean).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found. Please sign up first."
        )

    if not user.otp_hash or not user.otp_expires_at:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No pending verification code found. Please request a new code."
        )

    now_utc = datetime.datetime.now(datetime.timezone.utc)
    is_expired = False
    if user.otp_expires_at.tzinfo is not None:
        is_expired = now_utc > user.otp_expires_at
    else:
        is_expired = datetime.datetime.utcnow() > user.otp_expires_at

    if is_expired:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Verification code has expired. Please request a new code."
        )

    if (user.otp_attempts or 0) >= 5:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Too many incorrect attempts. Please request a new verification code."
        )

    if not verify_password(payload.otp.strip(), user.otp_hash):
        user.otp_attempts = (user.otp_attempts or 0) + 1
        db.commit()
        remaining = max(0, 5 - user.otp_attempts)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid verification code. ({remaining} attempts remaining)"
        )

    # Verification successful
    user.is_verified = True
    user.otp_hash = None
    user.otp_expires_at = None
    user.otp_attempts = 0
    user.last_login_at = datetime.datetime.utcnow()
    db.commit()
    db.refresh(user)

    access_token = create_access_token(data={"sub": str(user.id), "email": user.email})
    return Token(
        access_token=access_token,
        token_type="bearer",
        name=user.name,
        user=UserOut.from_orm(user)
    )


@router.post("/resend-otp")
def resend_otp(payload: ResendOtpRequest, db: Session = Depends(get_db)):
    email_clean = payload.email.lower().strip()
    user = db.query(User).filter(User.email == email_clean).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found with this email address."
        )

    otp = generate_six_digit_otp()
    user.otp_hash = hash_password(otp)
    user.otp_expires_at = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    user.otp_attempts = 0
    db.commit()
    db.refresh(user)

    send_otp_email(to_email=email_clean, name=user.name, otp=otp)

    return {
        "success": True,
        "message": "A fresh 6-digit verification code has been sent to your email."
    }


@router.post("/login", response_model=Token)
def login(user_in: UserLogin, db: Session = Depends(get_db)):
    email_clean = user_in.email.lower().strip()
    user = db.query(User).filter(User.email == email_clean).first()
    if not user or not verify_password(user_in.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password."
        )

    if not user.is_verified:
        # Automatically generate and send fresh OTP
        otp = generate_six_digit_otp()
        user.otp_hash = hash_password(otp)
        user.otp_expires_at = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        user.otp_attempts = 0
        db.commit()
        send_otp_email(to_email=email_clean, name=user.name, otp=otp)

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="email_not_verified"
        )

    user.last_login_at = datetime.datetime.utcnow()
    db.commit()

    access_token = create_access_token(data={"sub": str(user.id), "email": user.email})
    return Token(
        access_token=access_token,
        token_type="bearer",
        name=user.name,
        user=UserOut.from_orm(user)
    )


@router.get("/me", response_model=UserOut)
def me(current_user: User = Depends(get_current_user)):
    return UserOut.from_orm(current_user)
