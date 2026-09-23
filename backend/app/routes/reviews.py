from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload

from app.database import get_db
from app.models import Project, Review, User
from app.schemas import (
    ReviewCreate,
    ReviewStatusUpdate,
    ReviewOut,
    PendingReviewOut,
)
from app.routes.auth import get_current_user, get_current_admin

router = APIRouter(tags=["reviews"])


# -------------------------------------------------------------
# Client Endpoint: Submit Review for Own Completed Project
# -------------------------------------------------------------
@router.post("/projects/{project_id}/review", response_model=ReviewOut, status_code=status.HTTP_201_CREATED)
def submit_project_review(
    project_id: str,
    review_in: ReviewCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Client submits a review for a completed project they own.
    Enforces ownership, completed project status, and one review per project.
    Review is stored with status='pending' until moderated by admin.
    """
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with id {project_id} not found."
        )

    # 1. Enforce ownership server-side (never trust request body user_id)
    if project.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to review a project that does not belong to you."
        )

    # 2. Enforce completed status
    if project.status not in ["completed", "published"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Reviews can only be submitted for completed projects."
        )

    # 3. Enforce single review per project
    existing_review = db.query(Review).filter(Review.project_id == project_id).first()
    if existing_review:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A review has already been submitted for this project."
        )

    # 4. Create pending review
    review = Review(
        project_id=project.id,
        user_id=current_user.id,
        rating=review_in.rating,
        review_text=review_in.review_text.strip(),
        status="pending",
        submitted_at=datetime.utcnow(),
    )
    db.add(review)
    db.commit()
    db.refresh(review)
    return review


# -------------------------------------------------------------
# Admin Endpoints: Review Moderation
# -------------------------------------------------------------
@router.get("/admin/reviews/pending", response_model=List[PendingReviewOut])
def list_pending_reviews(
    current_admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Admin: List all reviews awaiting moderation.
    """
    reviews = (
        db.query(Review)
        .options(joinedload(Review.user), joinedload(Review.project))
        .filter(Review.status == "pending")
        .order_by(Review.submitted_at.desc())
        .all()
    )

    result = []
    for rev in reviews:
        result.append(
            PendingReviewOut(
                id=rev.id,
                project_id=rev.project_id,
                project_title=rev.project.title if rev.project else "Unknown Project",
                service_slug=rev.project.service_slug if rev.project else "",
                user_id=rev.user_id,
                client_name=rev.user.name if rev.user else "Unknown Client",
                rating=rev.rating,
                review_text=rev.review_text,
                status=rev.status,
                submitted_at=rev.submitted_at,
            )
        )
    return result


@router.patch("/admin/reviews/{review_id}", response_model=ReviewOut)
def moderate_review(
    review_id: str,
    status_in: ReviewStatusUpdate,
    current_admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Admin: Approve or reject a submitted review.
    Approving automatically moves the linked Project from 'completed' to 'published'.
    """
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Review with id {review_id} not found."
        )

    new_status = status_in.status.lower()
    if new_status not in ["approved", "rejected", "pending"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Status must be one of: approved, rejected, pending"
        )

    review.status = new_status
    review.reviewed_at = datetime.utcnow()

    # If approved, automatically transition linked project to 'published'
    project = db.query(Project).filter(Project.id == review.project_id).first()
    if project:
        if new_status == "approved":
            project.status = "published"
            if not project.completed_at:
                project.completed_at = datetime.utcnow()
        elif new_status == "rejected" and project.status == "published":
            project.status = "completed"

    db.commit()
    db.refresh(review)
    return review
