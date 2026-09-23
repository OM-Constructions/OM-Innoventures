import datetime
import uuid
from typing import Optional, List, Union, Any
from pydantic import BaseModel, EmailStr, Field


# Auth Schemas
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100)
    phone: Optional[str] = Field(None, max_length=50)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class VerifyOtpRequest(BaseModel):
    email: EmailStr
    otp: str = Field(..., min_length=6, max_length=6)


class ResendOtpRequest(BaseModel):
    email: EmailStr


class SignupResponse(BaseModel):
    success: bool = True
    requires_otp: bool = True
    email: str
    message: str


class UserOut(BaseModel):
    id: Union[str, int, uuid.UUID]
    name: str
    email: str
    phone: Optional[str] = None
    created_at: Optional[datetime.datetime] = None

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    name: Optional[str] = None
    user: UserOut


# Enquiry Schemas
class EnquiryCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=120)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=50)
    service: Optional[str] = Field(None, max_length=100)
    service_slug: Optional[str] = Field(None, max_length=100)
    location: Optional[str] = Field(None, max_length=200)
    website: Optional[str] = Field(None, max_length=200)
    honeypot: Optional[str] = Field(None, max_length=200)
    message: str = Field(..., min_length=3)


class EnquiryOut(BaseModel):
    id: Union[str, int, uuid.UUID]
    user_id: Optional[Union[str, int, uuid.UUID]] = None
    name: str
    email: str
    phone: Optional[str] = None
    service_slug: Optional[str] = None
    message: str
    status: str
    created_at: Optional[datetime.datetime] = None

    class Config:
        from_attributes = True


# Review Schemas
class ReviewCreate(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    review_text: str = Field(..., min_length=5, max_length=2000)


class ReviewStatusUpdate(BaseModel):
    status: str = Field(..., pattern="^(approved|rejected|pending)$")


class ReviewOut(BaseModel):
    id: Union[str, int, uuid.UUID]
    project_id: Union[str, int, uuid.UUID]
    user_id: Union[str, int, uuid.UUID]
    rating: int
    review_text: str
    status: str
    submitted_at: Optional[datetime.datetime] = None
    reviewed_at: Optional[datetime.datetime] = None

    class Config:
        from_attributes = True


class PendingReviewOut(BaseModel):
    id: Union[str, int, uuid.UUID]
    project_id: Union[str, int, uuid.UUID]
    project_title: str
    service_slug: str
    user_id: Union[str, int, uuid.UUID]
    client_name: str
    rating: int
    review_text: str
    status: str
    submitted_at: Optional[datetime.datetime] = None


# Project Schemas
class ProjectCreate(BaseModel):
    user_id: Union[str, int, uuid.UUID]
    enquiry_id: Optional[Union[str, int, uuid.UUID]] = None
    title: str = Field(..., min_length=2, max_length=200)
    service_slug: str = Field(..., min_length=2, max_length=100)
    summary: Optional[str] = Field(None, max_length=1000)


class ProjectStatusUpdate(BaseModel):
    status: str = Field(..., pattern="^(in_progress|completed|published)$")


class ProjectOut(BaseModel):
    id: Union[str, int, uuid.UUID]
    user_id: Union[str, int, uuid.UUID]
    enquiry_id: Optional[Union[str, int, uuid.UUID]] = None
    title: str
    service_slug: str
    summary: Optional[str] = None
    status: str
    completed_at: Optional[datetime.datetime] = None
    created_at: Optional[datetime.datetime] = None
    review: Optional[ReviewOut] = None

    class Config:
        from_attributes = True


class PublishedProjectOut(BaseModel):
    id: Union[str, int, uuid.UUID]
    title: str
    service_slug: str
    summary: Optional[str] = None
    client_display_name: str
    rating: Optional[int] = None
    review_text: Optional[str] = None
    status: str = "published"
    completed_at: Optional[datetime.datetime] = None
