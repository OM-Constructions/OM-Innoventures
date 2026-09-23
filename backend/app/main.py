import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.config import settings
from app.database import engine, Base
import app.models  # ensure models are registered
from app.routes import auth, contact, me, assistant, projects, reviews
from app.services.service_catalog import get_all_services, get_service, SERVICES
from app.services.company_info import COMPANY_INFO

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="Backend API for OM Innoventures & Build AI Technologies",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routers (mounted on /api and /api/v1 for compatibility)
for prefix in [settings.API_V1_STR, "/api/v1"]:
    app.include_router(auth.router, prefix=prefix)
    app.include_router(contact.router, prefix=prefix)
    app.include_router(me.router, prefix=prefix)
    app.include_router(assistant.router, prefix=prefix)
    app.include_router(projects.router, prefix=prefix)
    app.include_router(reviews.router, prefix=prefix)


for prefix in [settings.API_V1_STR, "/api/v1"]:
    @app.get(f"{prefix}/services", include_in_schema=(prefix == settings.API_V1_STR))
    def list_services_fn():
        return {"services": get_all_services()}

    @app.get(f"{prefix}/services/{{slug}}", include_in_schema=(prefix == settings.API_V1_STR))
    def get_service_detail_fn(slug: str):
        return get_service(slug)

    @app.get(f"{prefix}/company", include_in_schema=(prefix == settings.API_V1_STR))
    def get_company_details_fn():
        return COMPANY_INFO

    @app.get(f"{prefix}/health", include_in_schema=(prefix == settings.API_V1_STR))
    def health_check_fn():
        return {"status": "ok", "project": settings.PROJECT_NAME, "version": settings.PROJECT_VERSION}
def health_check():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION
    }


# Mount Frontend static files for unified local development
FRONTEND_DIR = Path(__file__).resolve().parent.parent.parent / "frontend"

if FRONTEND_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

    @app.get("/")
    def serve_index():
        index_file = FRONTEND_DIR / "index.html"
        if index_file.exists():
            return FileResponse(index_file)
        return {"status": "healthy", "service": settings.PROJECT_NAME, "version": settings.PROJECT_VERSION}

    @app.get("/login")
    @app.get("/login.html")
    def serve_login():
        return FileResponse(FRONTEND_DIR / "login.html")

    @app.get("/signup")
    @app.get("/signup.html")
    def serve_signup():
        return FileResponse(FRONTEND_DIR / "signup.html")

    @app.get("/my-requests")
    @app.get("/my-requests.html")
    def serve_my_requests():
        return FileResponse(FRONTEND_DIR / "my-requests.html")

    @app.get("/technical-documents")
    @app.get("/technical-documents.html")
    def serve_technical_documents():
        return FileResponse(FRONTEND_DIR / "technical-documents.html")

    # Serve service detail pages
    @app.get("/services/{slug}")
    @app.get("/services/{slug}/")
    @app.get("/services/{slug}/index.html")
    def serve_service_page(slug: str):
        service_file = FRONTEND_DIR / "services" / slug / "index.html"
        if service_file.exists():
            return FileResponse(service_file)
        return FileResponse(FRONTEND_DIR / "index.html")

    # Catch-all for assets (css, js, images, etc.)
    app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend_root")
else:
    @app.get("/")
    def serve_api_root():
        return {
            "status": "healthy",
            "service": settings.PROJECT_NAME,
            "version": settings.PROJECT_VERSION,
            "docs": "/docs",
            "api_v1": settings.API_V1_STR
        }

