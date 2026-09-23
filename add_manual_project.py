"""
Helper script to manually add real Projects and Client Reviews into the OM Innoventures database.
Run with: python3 add_manual_project.py
"""

import os
import sys
import uuid
import datetime

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend'))

from app.database import SessionLocal
from app.models import User, Project, Review

def create_manual_project():
    db = SessionLocal()
    try:
        print("\n=== OM Innoventures: Add Real Project Manually ===")
        
        # 1. Select or Create User (Client)
        users = db.query(User).all()
        print(f"\nExisting verified users / clients ({len(users)} found):")
        for idx, u in enumerate(users, 1):
            print(f"  [{idx}] {u.name} ({u.email})")
        print("  [N] Create New Client Account")

        user_choice = input("\nSelect client [number or N]: ").strip()
        user_id = None
        
        if user_choice.lower() == 'n' or not users:
            name = input("Client Full Name: ").strip()
            email = input("Client Email: ").strip()
            phone = input("Client Phone (optional): ").strip() or None
            
            # Check if user already exists
            existing = db.query(User).filter(User.email == email).first()
            if existing:
                user_id = existing.id
                print(f"Found existing client with email: {email}")
            else:
                from app.routes.auth import get_password_hash
                new_user = User(
                    name=name,
                    email=email,
                    phone=phone,
                    password_hash=get_password_hash("ClientPassword123!"),
                    is_verified=True
                )
                db.add(new_user)
                db.commit()
                db.refresh(new_user)
                user_id = new_user.id
                print(f"✓ Created client: {name} (ID: {user_id})")
        else:
            try:
                selected_idx = int(user_choice) - 1
                user_id = users[selected_idx].id
                print(f"Selected client: {users[selected_idx].name}")
            except Exception:
                print("Invalid selection. Exiting.")
                return

        # 2. Project Details
        print("\n--- Project Details ---")
        title = input("Project Title (e.g. Enterprise Data Lake & AI Dashboard): ").strip()
        if not title:
            print("Title cannot be empty.")
            return

        print("\nServices: data-analytics-bi, data-science, ai-ml-solutions, software-development,")
        print("          full-stack-development, product-development, ui-ux-design, graphic-design,")
        print("          finance-accounting, auditing-assurance, cybersecurity, saas-ai-solutions")
        service_slug = input("Service Slug [default: data-analytics-bi]: ").strip() or "data-analytics-bi"
        summary = input("Project Summary / Deliverable Scope: ").strip()
        
        status_choice = input("Project Status (1: in_progress, 2: completed, 3: published) [default: 3]: ").strip() or "3"
        status_map = {"1": "in_progress", "2": "completed", "3": "published"}
        proj_status = status_map.get(status_choice, "published")

        project = Project(
            user_id=user_id,
            title=title,
            service_slug=service_slug,
            summary=summary if summary else None,
            status=proj_status,
            completed_at=datetime.datetime.utcnow() if proj_status in ["completed", "published"] else None
        )
        db.add(project)
        db.commit()
        db.refresh(project)
        print(f"\n✓ Successfully created project: '{title}' (ID: {project.id}, Status: {proj_status})")

        # 3. Optional Client Review
        if proj_status in ["completed", "published"]:
            add_rev = input("\nDo you want to attach a verified client review? (y/n) [default: y]: ").strip().lower()
            if add_rev != 'n':
                rating_in = input("Rating (1 to 5) [default: 5]: ").strip() or "5"
                try:
                    rating = max(1, min(5, int(rating_in)))
                except ValueError:
                    rating = 5
                review_text = input("Client Review Text / Testimonial: ").strip()
                if review_text:
                    review = Review(
                        project_id=project.id,
                        user_id=user_id,
                        rating=rating,
                        review_text=review_text,
                        status="approved",
                        reviewed_at=datetime.datetime.utcnow()
                    )
                    db.add(review)
                    db.commit()
                    print(f"✓ Attached verified {rating}★ review to project!")

        print("\n All set! The project will now be visible in the Client Portal and on the website portfolio.")

    except Exception as e:
        db.rollback()
        print(f"Error creating project: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    create_manual_project()
