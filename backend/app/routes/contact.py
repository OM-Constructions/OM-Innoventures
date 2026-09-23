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

    email_clean = enquiry_in.email.lower().strip()
    
    # Determine user_id: either from auth token or match existing user by email
    user_id = None
    if current_user:
        user_id = str(current_user.id)
    else:
        matched_user = db.query(User).filter(User.email == email_clean).first()
        if matched_user:
            user_id = str(matched_user.id)

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

    # Dispatch email notification asynchronously in background
    email_data = {
        "id": str(enquiry.id),
        "name": enquiry.name,
        "email": enquiry.email,
        "phone": enquiry.phone,
        "service": enquiry.service_slug,
        "message": enquiry.message,
        "client_ip": enquiry.ip_address,
    }
    background_tasks.add_task(notify_new_enquiry, email_data)

    service_info = get_service(enquiry.service_slug)

    return {
        "success": True,
        "message": "Thanks — we've received your project details and sent you a confirmation email. Our senior AI & software team will review your scope and get in touch within 24 hours.",
        "enquiry_id": str(enquiry.id),
        "service": {
            "slug": service_info.get("slug", service_val),
            "name": service_info.get("name", service_val),
            "client_line": service_info.get("client_line", "")
        },
        "email_status": {"queued": True}
    }
