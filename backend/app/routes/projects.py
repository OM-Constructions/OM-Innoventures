from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload

from app.database import get_db
from app.models import Project, Review, User, Enquiry
from app.schemas import (
    ProjectCreate,
    ProjectStatusUpdate,
    ProjectOut,
    PublishedProjectOut,
    ReviewOut,
)
from app.routes.auth import get_current_user, get_current_admin

router = APIRouter(tags=["projects"])


def format_client_display_name(full_name: Optional[str]) -> str:
    """Format full client name to 'First L.' for privacy preservation."""
    if not full_name:
        return "Verified Client"
    parts = full_name.strip().split()
    if len(parts) == 1:
        return parts[0].capitalize()
    first = parts[0].capitalize()
    last_initial = parts[-1][0].upper() + "."
    return f"{first} {last_initial}"


# -------------------------------------------------------------
# Public Endpoint: Published Projects
# -------------------------------------------------------------
@router.get("/projects/published", response_model=List[PublishedProjectOut])
def get_published_projects(
    service_slug: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Publicly list all projects marked as 'published' (completed + approved review).
    Anonymizes client name to First Name + Last Initial.
    """
    query = (
        db.query(Project)
        .options(joinedload(Project.user), joinedload(Project.review))
        .filter(Project.status == "published")
    )
    if service_slug:
        query = query.filter(Project.service_slug == service_slug)

    projects = query.order_by(Project.completed_at.desc(), Project.id.desc()).all()

    result = []
    for proj in projects:
        # Check that there is an approved review attached
        review = proj.review
        rating = review.rating if review and review.status == "approved" else None
        review_text = review.review_text if review and review.status == "approved" else None
        display_name = format_client_display_name(proj.user.name if proj.user else None)

        result.append(
            PublishedProjectOut(
                id=proj.id,
                title=proj.title,
                service_slug=proj.service_slug,
                summary=proj.summary,
                status=proj.status,
                completed_at=proj.completed_at,
                client_display_name=display_name,
                rating=rating,
                review_text=review_text,
            )
        )
    return result


# -------------------------------------------------------------
# Client-Protected Endpoint: Own Projects
# -------------------------------------------------------------
@router.get("/projects/me", response_model=List[ProjectOut])
def get_my_projects(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Return all projects belonging to the logged-in client.
    Used by the client dashboard to prompt for reviews on completed projects.
    """
    projects = (
        db.query(Project)
        .options(joinedload(Project.review))
        .filter(Project.user_id == current_user.id)
        .order_by(Project.created_at.desc())
        .all()
    )
    return projects


# -------------------------------------------------------------
# Admin Endpoints: Project Management
# -------------------------------------------------------------
@router.post("/admin/projects", response_model=ProjectOut, status_code=status.HTTP_201_CREATED)
def create_project(
    project_in: ProjectCreate,
    current_admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Admin: Create a new project for a verified client.
    Optionally links to an existing enquiry_id.
    """
    client = db.query(User).filter(User.id == project_in.user_id).first()
    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {project_in.user_id} not found."
        )

    if project_in.enquiry_id:
        enquiry = db.query(Enquiry).filter(Enquiry.id == project_in.enquiry_id).first()
        if not enquiry:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Enquiry with id {project_in.enquiry_id} not found."
            )

    project = Project(
        user_id=project_in.user_id,
        enquiry_id=project_in.enquiry_id,
        title=project_in.title.strip(),
        service_slug=project_in.service_slug.strip(),
        summary=project_in.summary.strip() if project_in.summary else None,
        status="in_progress",
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


@router.patch("/admin/projects/{project_id}/status", response_model=ProjectOut)
def update_project_status(
    project_id: str,
    status_in: ProjectStatusUpdate,
    current_admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Admin: Update a project's status (e.g., in_progress -> completed).
    When marked completed, completed_at is automatically recorded.
    """
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with id {project_id} not found."
        )

    new_status = status_in.status.lower()
    if new_status not in ["in_progress", "completed", "published"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Status must be one of: in_progress, completed, published"
        )

    project.status = new_status
    if new_status in ["completed", "published"] and not project.completed_at:
        project.completed_at = datetime.utcnow()

    db.commit()
    db.refresh(project)
    return project
