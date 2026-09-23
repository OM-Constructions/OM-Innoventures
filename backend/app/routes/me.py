from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List

from app.database import get_db
from app.models import User, Enquiry
from app.schemas import EnquiryOut
from app.routes.auth import get_current_user

router = APIRouter(prefix="/me", tags=["me"])


@router.get("/requests", response_model=List[EnquiryOut])
def get_my_enquiries(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Fetch all enquiries matching either user_id OR client email
    enquiries = (
        db.query(Enquiry)
        .filter(or_(Enquiry.user_id == current_user.id, Enquiry.email == current_user.email))
        .order_by(Enquiry.created_at.desc())
        .all()
    )
    return enquiries
