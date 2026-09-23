import os
import sys
from pathlib import Path

# Add backend to sys.path
backend_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(backend_dir))

from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

client = TestClient(app)

def test_api_flow():
    print("Testing health check...")
    resp = client.get("/api/health")
    assert resp.status_code == 200, resp.text
    print("Health OK:", resp.json())

    print("Testing services listing...")
    resp = client.get("/api/services")
    assert resp.status_code == 200, resp.text
    services = resp.json()["services"]
    assert len(services) == 11
    print(f"Services catalog loaded with {len(services)} services.")

    print("Testing company info...")
    resp = client.get("/api/company")
    assert resp.status_code == 200
    assert resp.json()["founder"]["name"] == "Kishor Kumar A"
    print("Company info OK.")

    # Test client registration
    test_email = "tester@innoventures.ai"
    print("Testing client signup...")
    signup_payload = {
        "name": "Test Client",
        "email": test_email,
        "password": "Password123!",
        "phone": "+91 9988776655"
    }
    resp = client.post("/api/auth/signup", json=signup_payload)
    if resp.status_code == 400 and "already exists" in resp.text:
        # login instead
        print("User already exists, testing login...")
        resp = client.post("/api/auth/login", json={"email": test_email, "password": "Password123!"})
    
    assert resp.status_code in [200, 201], resp.text
    auth_data = resp.json()
    token = auth_data["access_token"]
    assert token is not None
    print("Auth token obtained successfully.")

    # Test submitting an enquiry
    print("Testing enquiry submission...")
    enquiry_payload = {
        "name": "Test Client",
        "email": test_email,
        "phone": "+91 9988776655",
        "service": "ai-ml-solutions",
        "message": "We require an enterprise RAG knowledge base for 50,000 legal and technical docs."
    }
    resp = client.post("/api/contact", json=enquiry_payload, headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 201, resp.text
    enquiry_resp = resp.json()
    assert enquiry_resp["success"] is True
    print("Enquiry submitted successfully. Response:", enquiry_resp["message"])

    # Test fetching enquiries for client
    print("Testing GET /api/me/requests...")
    resp = client.get("/api/me/requests", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200, resp.text
    requests_list = resp.json()
    assert len(requests_list) >= 1
    print(f"Retrieved {len(requests_list)} enquiries for current user. Latest status: {requests_list[0]['status']}")

    # Test AI assistant endpoint
    print("Testing AI assistant...")
    resp = client.post("/api/assistant", json={"query": "What demos do you have?"})
    assert resp.status_code == 200
    print("Assistant reply:", resp.json()["reply"][:90], "...")

    # ========================================================
    # PROJECT & CLIENT-REVIEW SYSTEM TESTS
    # ========================================================
    admin_headers = {"X-Admin-Key": "om-admin-secure-key-2025"}

    print("\n--- Testing Project & Client-Review Flow ---")

    # 1. Fetch published projects initially (should be empty if clean db)
    resp = client.get("/api/v1/projects/published")
    assert resp.status_code == 200, resp.text
    initial_published = resp.json()
    print(f"Initially published projects count: {len(initial_published)}")

    # 2. Get client user id from /api/auth/me
    resp = client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    client_user_id = resp.json()["id"]

    # 3. Admin creates a project for this client
    project_payload = {
        "user_id": client_user_id,
        "title": "Enterprise RAG Intelligence System",
        "service_slug": "ai-ml-solutions",
        "summary": "Custom enterprise knowledge indexing and multimodal LLM pipeline built with FastAPI and Qdrant."
    }
    resp = client.post("/api/v1/admin/projects", json=project_payload, headers=admin_headers)
    assert resp.status_code == 201, resp.text
    project_data = resp.json()
    project_id = project_data["id"]
    assert project_data["status"] == "in_progress"
    print(f"Admin created Project ID {project_id} in status: {project_data['status']}")

    # 4. Client views their projects via GET /api/v1/projects/me
    resp = client.get("/api/v1/projects/me", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    client_projects = resp.json()
    assert any(p["id"] == project_id for p in client_projects)
    print(f"Client can see their project in my-requests: {project_data['title']}")

    # 5. Client attempts to review in_progress project -> must fail (400)
    review_payload = {
        "rating": 5,
        "review_text": "Exceptional AI architecture and delivered ahead of schedule!"
    }
    resp = client.post(f"/api/v1/projects/{project_id}/review", json=review_payload, headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 400, "Should reject review for in_progress project"
    print("Correctly rejected review submission for in_progress project.")

    # 6. Unauthorized user attempts to review project -> must fail (403)
    # Create second user
    other_email = "other@innoventures.ai"
    resp = client.post("/api/auth/signup", json={"name": "Other User", "email": other_email, "password": "Password123!"})
    if resp.status_code == 400:
        resp = client.post("/api/auth/login", json={"email": other_email, "password": "Password123!"})
    other_token = resp.json()["access_token"]

    # 7. Admin marks project as 'completed'
    resp = client.patch(f"/api/v1/admin/projects/{project_id}/status", json={"status": "completed"}, headers=admin_headers)
    assert resp.status_code == 200
    assert resp.json()["status"] == "completed"
    assert resp.json()["completed_at"] is not None
    print(f"Admin marked Project ID {project_id} as completed.")

    # 8. Non-owner attempts to review completed project -> 403 Forbidden
    resp = client.post(f"/api/v1/projects/{project_id}/review", json=review_payload, headers={"Authorization": f"Bearer {other_token}"})
    assert resp.status_code == 403, "Should reject review from non-owner"
    print("Correctly rejected review submission from non-owner (403).")

    # 9. Legitimate client submits review for completed project -> status="pending"
    resp = client.post(f"/api/v1/projects/{project_id}/review", json=review_payload, headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 201, resp.text
    review_data = resp.json()
    review_id = review_data["id"]
    assert review_data["status"] == "pending"
    print(f"Client submitted Review ID {review_id} (status: pending).")

    # 10. Attempt duplicate review on same project -> must fail (400)
    resp = client.post(f"/api/v1/projects/{project_id}/review", json=review_payload, headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 400, "Should reject duplicate review on same project"
    print("Correctly rejected duplicate review submission (400).")

    # 11. Check public published projects -> project should NOT be visible yet
    resp = client.get("/api/v1/projects/published")
    assert resp.status_code == 200
    published_now = resp.json()
    assert not any(p["id"] == project_id for p in published_now)
    print("Verified pending review project is NOT visible on public endpoint.")

    # 12. Admin lists pending reviews
    resp = client.get("/api/v1/admin/reviews/pending", headers=admin_headers)
    assert resp.status_code == 200
    pending_list = resp.json()
    assert any(r["id"] == review_id for r in pending_list)
    print(f"Admin successfully fetched {len(pending_list)} pending reviews for moderation.")

    # 13. Admin approves the review -> triggers project status -> 'published'
    resp = client.patch(f"/api/v1/admin/reviews/{review_id}", json={"status": "approved"}, headers=admin_headers)
    assert resp.status_code == 200
    assert resp.json()["status"] == "approved"
    print(f"Admin approved Review ID {review_id}.")

    # 14. Verify Project is now returned on public published endpoint with privacy anonymization
    resp = client.get("/api/v1/projects/published")
    assert resp.status_code == 200
    published_list = resp.json()
    pub_proj = next((p for p in published_list if p["id"] == project_id), None)
    assert pub_proj is not None, "Project must now be in published list"
    assert pub_proj["client_display_name"] == "Test C.", f"Expected 'Test C.' got '{pub_proj['client_display_name']}'"
    assert pub_proj["rating"] == 5
    assert "Exceptional AI architecture" in pub_proj["review_text"]
    # Check that privacy is strictly maintained (no email, no phone)
    assert "email" not in pub_proj
    assert "phone" not in pub_proj
    print(f"Public published project verified successfully: {pub_proj['title']} by {pub_proj['client_display_name']} ({pub_proj['rating']}★)")

    print("\nALL TESTS INCLUDING PROJECT & REVIEW SYSTEM PASSED! 🚀✅")

if __name__ == "__main__":
    test_api_flow()
