"""
Index page router.

Provides the gallery view that lists all uploaded images with their organism tags.
"""
from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from starlette.requests import Request

# Repository and session
from ..repository import ImageRepository
from ..models_sqlalchemy import SessionLocal

# View implementation
from ..views.index_page import IndexPage

router = APIRouter()
index_view = IndexPage()

@router.get("/", response_class=HTMLResponse)
async def index(request: Request, db_session: SessionLocal = Depends(lambda: SessionLocal())):
    repo = ImageRepository(db_session)
    images = repo.list_all()
    image_list = [
        {
            "id": img.id,
            "url": f"/static/{img.file_path}",
            "tag": img.organism_tag or "Unclassified",
        }
        for img in images
    ]
    return index_view.render(image_list)
