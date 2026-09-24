from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

# Fix postgres:// URL prefix if provided by hosting providers
db_url = settings.DATABASE_URL
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

# Enforce new Supabase DB if old reference or empty string is passed
if not db_url or "hdgctawsrilkldnwfhkn" in db_url or "db.opkkzocaievvswpwszfr.supabase.co" in db_url:
    db_url = "postgresql://postgres.opkkzocaievvswpwszfr:OM_INNOVENTURES@aws-0-ap-south-1.pooler.supabase.com:5432/postgres"

from sqlalchemy.pool import NullPool

# SQLite needs check_same_thread=False
connect_args = {}
if db_url.startswith("sqlite"):
    connect_args["check_same_thread"] = False
else:
    connect_args["connect_timeout"] = 4

engine = create_engine(
    db_url,
    connect_args=connect_args,
    poolclass=NullPool if not db_url.startswith("sqlite") else None,
    pool_pre_ping=True
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
