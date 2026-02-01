"""
Material database model and Pydantic schemas.
"""
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
import uuid
import enum
from app.core.database import Base


class MaterialCategory(str, enum.Enum):
    """Material category enumeration."""
    THEORY = "theory"
    LAB = "lab"


class Material(Base):
    """Material database model."""
    __tablename__ = "materials"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    file_path = Column(String(500), nullable=False)
    file_type = Column(String(50), nullable=False)
    category = Column(String(20), nullable=False)
    week = Column(Integer, nullable=True)
    topic = Column(String(255), nullable=True)
    tags = Column(ARRAY(Text), nullable=True)
    uploaded_by = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# Pydantic Schemas
class MaterialBase(BaseModel):
    """Base material schema."""
    title: str
    description: Optional[str] = None
    category: MaterialCategory
    week: Optional[int] = None
    topic: Optional[str] = None
    tags: Optional[List[str]] = None


class MaterialCreate(MaterialBase):
    """Schema for material creation (file uploaded separately)."""
    pass


class MaterialUpdate(BaseModel):
    """Schema for material update."""
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[MaterialCategory] = None
    week: Optional[int] = None
    topic: Optional[str] = None
    tags: Optional[List[str]] = None


class MaterialResponse(MaterialBase):
    """Schema for material response."""
    id: uuid.UUID
    file_path: str
    file_type: str
    uploaded_by: Optional[uuid.UUID]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class MaterialListResponse(BaseModel):
    """Schema for paginated material list."""
    total: int
    page: int
    page_size: int
    materials: List[MaterialResponse]
