import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "OM Innoventures & Build AI Technologies"
    PROJECT_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    
    # Security / Auth
    JWT_SECRET: str = os.getenv("JWT_SECRET", "om-innoventures-ai-secret-key-super-secure-2025-x9")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    ADMIN_SECRET_KEY: str = os.getenv("ADMIN_SECRET_KEY", "om-admin-secure-key-2025")
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./om_innoventures.db")
    
    # Email notifications (Dedicated Tech Inbox)
    COMPANY_NOTIFICATION_EMAIL: str = os.getenv("COMPANY_NOTIFICATION_EMAIL", "ominnoventuresaitech@gmail.com")
    SMTP_HOST: str = os.getenv("SMTP_HOST", "")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER: str = os.getenv("SMTP_USER", "")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")
    SMTP_FROM_NAME: str = os.getenv("SMTP_FROM_NAME", "OM Innoventures & Build AI Technologies")
    
    #  cross-link
    _SITE_URL: str = "https://om-buildings.vercel.app/"
    
    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
