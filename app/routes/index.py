"""
Index page router.

Provides the gallery view that lists all uploaded images with their organism tags.
"""
from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

# Assume we have a repository to fetch images
from ..repository import ImageRepository
from ..models_sqlalchemy import SessionLocal  # SQLAlchemy session factory

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request, db_session: SessionLocal = Depends(SessionLocal)):
    repo = ImageRepository(db_session)
    images = repo.list_all()
    # Convert to simple dicts for template context
    image_list = [
        {
            "id": img.id,
            "url": f"/static/{img.file_path}",
            "tag": img.organism_tag or "Unclassified",
        }
        for img in images
    ]
    return templates.TemplateResponse("index.html", {"request": request, "images": image_list})
