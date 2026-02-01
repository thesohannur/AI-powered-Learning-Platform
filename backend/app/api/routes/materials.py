"""
Materials routes for file upload and management.
"""
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form, Query
from sqlalchemy.orm import Session
from typing import Optional, List
import os
import uuid
import shutil
from pathlib import Path
from app.core.database import get_db
from app.core.config import settings
from app.models.material import Material, MaterialCreate, MaterialResponse, MaterialListResponse, MaterialCategory, MaterialUpdate
from app.models.user import User
from app.api.dependencies import get_current_user, get_current_admin

router = APIRouter()

# Ensure upload directory exists
UPLOAD_DIR = Path(settings.UPLOAD_DIR)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload", response_model=MaterialResponse, status_code=status.HTTP_201_CREATED)
async def upload_material(
    file: UploadFile = File(...),
    title: str = Form(...),
    description: Optional[str] = Form(None),
    category: MaterialCategory = Form(...),
    week: Optional[int] = Form(None),
    topic: Optional[str] = Form(None),
    tags: Optional[str] = Form(None),  # Comma-separated string
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """
    Upload a new material file (admin only).
    
    Args:
        file: File to upload
        title: Material title
        description: Material description
        category: Material category (theory/lab)
        week: Week number
        topic: Topic name
        tags: Comma-separated tags
        db: Database session
        current_user: Current authenticated admin user
    
    Returns:
        Created material object
    """
    # Validate file size
    file.file.seek(0, 2)  # Seek to end
    file_size = file.file.tell()
    file.file.seek(0)  # Reset to beginning
    
    if file_size > settings.MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File size exceeds maximum allowed size of {settings.MAX_UPLOAD_SIZE / (1024*1024)}MB"
        )
    
    # Generate unique filename
    file_extension = Path(file.filename).suffix
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = UPLOAD_DIR / unique_filename
    
    # Save file
    try:
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error saving file: {str(e)}"
        )
    
    # Parse tags
    tags_list = [tag.strip() for tag in tags.split(",")] if tags else None
    
    # Create material record
    new_material = Material(
        title=title,
        description=description,
        file_path=str(file_path),
        file_type=file.content_type or "application/octet-stream",
        category=category.value,
        week=week,
        topic=topic,
        tags=tags_list,
        uploaded_by=current_user.id
    )
    
    db.add(new_material)
    db.commit()
    db.refresh(new_material)
    
    return new_material


@router.get("/", response_model=MaterialListResponse)
async def list_materials(
    category: Optional[MaterialCategory] = Query(None),
    week: Optional[int] = Query(None),
    topic: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    List materials with optional filtering and pagination.
    
    Args:
        category: Filter by category
        week: Filter by week
        topic: Filter by topic
        search: Search in title and description
        page: Page number (1-based)
        page_size: Items per page
        db: Database session
        current_user: Current authenticated user
    
    Returns:
        Paginated list of materials
    """
    query = db.query(Material)
    
    # Apply filters
    if category:
        query = query.filter(Material.category == category.value)
    if week is not None:
        query = query.filter(Material.week == week)
    if topic:
        query = query.filter(Material.topic.ilike(f"%{topic}%"))
    if search:
        query = query.filter(
            (Material.title.ilike(f"%{search}%")) | 
            (Material.description.ilike(f"%{search}%"))
        )
    
    # Get total count
    total = query.count()
    
    # Apply pagination
    offset = (page - 1) * page_size
    materials = query.order_by(Material.created_at.desc()).offset(offset).limit(page_size).all()
    
    return MaterialListResponse(
        total=total,
        page=page,
        page_size=page_size,
        materials=materials
    )


@router.get("/{material_id}", response_model=MaterialResponse)
async def get_material(
    material_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get a specific material by ID.
    
    Args:
        material_id: Material UUID
        db: Database session
        current_user: Current authenticated user
    
    Returns:
        Material object
    """
    material = db.query(Material).filter(Material.id == material_id).first()
    
    if not material:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material not found"
        )
    
    return material


@router.put("/{material_id}", response_model=MaterialResponse)
async def update_material(
    material_id: str,
    material_update: MaterialUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """
    Update material metadata (admin only).
    
    Args:
        material_id: Material UUID
        material_update: Updated material data
        db: Database session
        current_user: Current authenticated admin user
    
    Returns:
        Updated material object
    """
    material = db.query(Material).filter(Material.id == material_id).first()
    
    if not material:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material not found"
        )
    
    # Update fields
    update_data = material_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if field == "category" and value:
            setattr(material, field, value.value)
        else:
            setattr(material, field, value)
    
    material.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(material)
    
    return material


@router.delete("/{material_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_material(
    material_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """
    Delete a material and its file (admin only).
    
    Args:
        material_id: Material UUID
        db: Database session
        current_user: Current authenticated admin user
    """
    material = db.query(Material).filter(Material.id == material_id).first()
    
    if not material:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material not found"
        )
    
    # Delete file from filesystem
    file_path = Path(material.file_path)
    if file_path.exists():
        file_path.unlink()
    
    # Delete database record
    db.delete(material)
    db.commit()
    
    return None


@router.get("/{material_id}/download")
async def download_material(
    material_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Download a material file.
    
    Args:
        material_id: Material UUID
        db: Database session
        current_user: Current authenticated user
    
    Returns:
        File response
    """
    from fastapi.responses import FileResponse
    
    material = db.query(Material).filter(Material.id == material_id).first()
    
    if not material:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material not found"
        )
    
    file_path = Path(material.file_path)
    if not file_path.exists():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="File not found on server"
        )
    
    # Get the original file extension from the stored file
    file_extension = file_path.suffix
    # Sanitize title for filename
    safe_title = material.title.replace('/', '-').replace('\\', '-')
    download_filename = f"{safe_title}{file_extension}"
    
    return FileResponse(
        path=str(file_path),
        filename=download_filename,
        media_type=material.file_type,
        headers={
            "Content-Disposition": f'attachment; filename="{download_filename}"'
        }
    )
