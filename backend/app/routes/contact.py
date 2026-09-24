import uuid
from fastapi import APIRouter, Depends, Request, status, BackgroundTasks
from sqlalchemy.orm import Session
from typing import Optional, Dict, Any

from app.database import get_db
from app.models import Enquiry, User
from app.schemas import EnquiryCreate, EnquiryOut
from app.routes.auth import get_current_user_optional
from app.services.email_service import notify_new_enquiry
from app.services.service_catalog import get_service

router = APIRouter(prefix="/contact", tags=["contact"])


@router.post("", status_code=status.HTTP_201_CREATED)
def submit_enquiry(
    enquiry_in: EnquiryCreate,
    request: Request,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_user_optional)
):
    # Spam honeypot trap
    if enquiry_in.honeypot or enquiry_in.website:
        return {
            "success": True,
            "message": "Enquiry received.",
            "enquiry_id": "ok"
        }

    # Detect client IP
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        client_ip = forwarded.split(",")[0].strip()
    else:
        client_ip = request.client.host if request.client else "127.0.0.1"

    # Attempt to determine user_id and persist enquiry to database
    enquiry_id = str(uuid.uuid4())
    db_saved = False

    try:
        user_id = None
        if current_user:
            user_id = str(current_user.id)
        else:
            try:
                matched_user = db.query(User).filter(User.email == email_clean).first()
                if matched_user:
                    user_id = str(matched_user.id)
            except Exception as lookup_err:
                print(f"[Warning] User lookup skipped due to DB error: {lookup_err}")

        service_val = (enquiry_in.service or enquiry_in.service_slug or "general-consultation").strip()

        enquiry = Enquiry(
            user_id=user_id,
            name=enquiry_in.name.strip(),
            email=email_clean,
            phone=enquiry_in.phone.strip() if enquiry_in.phone else None,
            service_slug=service_val,
            message=enquiry_in.message.strip(),
            status="Received",
            ip_address=client_ip,
        )
        db.add(enquiry)
        db.commit()
        db.refresh(enquiry)
        enquiry_id = str(enquiry.id)
        db_saved = True
    except Exception as db_err:
        print(f"[Warning] Database save error for enquiry: {db_err}")
        try:
            db.rollback()
        except Exception:
            pass
        service_val = (enquiry_in.service or enquiry_in.service_slug or "general-consultation").strip()

    # Dispatch email notification asynchronously in background
    email_data = {
        "id": enquiry_id,
        "name": enquiry_in.name.strip(),
        "email": email_clean,
        "phone": enquiry_in.phone.strip() if enquiry_in.phone else None,
        "service": service_val,
        "message": enquiry_in.message.strip(),
        "client_ip": client_ip,
    }
    try:
        background_tasks.add_task(notify_new_enquiry, email_data)
    except Exception as task_err:
        print(f"[Warning] Failed to enqueue email task: {task_err}")
        # Synchronous fallback dispatch
        try:
            notify_new_enquiry(email_data)
        except Exception as sync_err:
            print(f"[Warning] Synchronous email dispatch error: {sync_err}")

    service_info = get_service(service_val)

    return {
        "success": True,
        "message": "Thanks — we've received your project details and sent you a confirmation email. Our senior AI & software team will review your scope and get in touch within 24 hours.",
        "enquiry_id": enquiry_id,
        "service": {
            "slug": service_info.get("slug", service_val),
            "name": service_info.get("name", service_val),
            "client_line": service_info.get("client_line", "")
        },
        "db_saved": db_saved,
        "email_status": {"queued": True}
    }
