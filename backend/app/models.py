import datetime
import uuid
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Uuid
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = Column(String(64), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(200), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    phone = Column(String(50), nullable=True)
    is_verified = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_login_at = Column(DateTime, nullable=True)
    otp_hash = Column(String(255), nullable=True)
    otp_expires_at = Column(DateTime, nullable=True)
    otp_attempts = Column(Integer, default=0)

    @property
    def hashed_password(self):
        return self.password_hash

    @hashed_password.setter
    def hashed_password(self, value):
        self.password_hash = value

    enquiries = relationship("Enquiry", back_populates="user", cascade="all, delete-orphan")
    projects = relationship("Project", back_populates="user", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="user", cascade="all, delete-orphan")


class Enquiry(Base):
    __tablename__ = "enquiries"
    __table_args__ = {"extend_existing": True}

    id = Column(String(64), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(64), ForeignKey("users.id"), nullable=True)
    name = Column(String(200), nullable=False)
    email = Column(String(255), index=True, nullable=False)
    phone = Column(String(50), nullable=True)
    service_slug = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
    status = Column(String(50), default="Received")
    ip_address = Column(String(45), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    @property
    def service(self):
        return self.service_slug

    @service.setter
    def service(self, value):
        self.service_slug = value

    @property
    def client_ip(self):
        return self.ip_address

    @client_ip.setter
    def client_ip(self, value):
        self.ip_address = value

    user = relationship("User", back_populates="enquiries")


class Project(Base):
    __tablename__ = "projects"
    __table_args__ = {"extend_existing": True}

    id = Column(String(64), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(64), ForeignKey("users.id"), nullable=False, index=True)
    enquiry_id = Column(String(64), ForeignKey("enquiries.id"), nullable=True)
    title = Column(String(200), nullable=False)
    service_slug = Column(String(100), nullable=False)
    summary = Column(Text, nullable=True)
    status = Column(String(50), default="in_progress", index=True)  # in_progress, completed, published
    completed_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="projects")
    enquiry = relationship("Enquiry")
    review = relationship("Review", back_populates="project", uselist=False, cascade="all, delete-orphan")


class Review(Base):
    __tablename__ = "reviews"
    __table_args__ = {"extend_existing": True}

    id = Column(String(64), primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = Column(String(64), ForeignKey("projects.id"), unique=True, nullable=False, index=True)
    user_id = Column(String(64), ForeignKey("users.id"), nullable=False, index=True)
    rating = Column(Integer, nullable=False)  # 1 to 5
    review_text = Column(Text, nullable=False)
    status = Column(String(50), default="pending", index=True)  # pending, approved, rejected
    submitted_at = Column(DateTime, default=datetime.datetime.utcnow)
    reviewed_at = Column(DateTime, nullable=True)

    project = relationship("Project", back_populates="review")
    user = relationship("User", back_populates="reviews")
