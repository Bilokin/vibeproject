from fastapi import APIRouter, Request, File, UploadFile, Depends
from starlette.responses import RedirectResponse, HTMLResponse
import os
from ..models_sqlalchemy import Image, SessionLocal
from ..views.upload_page import UploadPage

router = APIRouter()

def get_user_email(request: Request):
    return request.cookies.get("user_email")

@router.get("/upload")
def upload_get(request: Request, user_email: str | None = Depends(get_user_email)):
    if not user_email:
        return RedirectResponse(url="/login", status_code=303)
    page = UploadPage()
    return HTMLResponse(content=page.render())

@router.post("/upload")
def upload_post(request: Request, file: UploadFile = File(...), user_email: str | None = Depends(get_user_email)):
    if not user_email:
        return RedirectResponse(url="/login", status_code=303)
    # Save file to static/uploads
    # Resolve uploads directory relative to project root
    # Resolve uploads directory relative to project root
    uploads_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "static", "uploads"))
    os.makedirs(uploads_dir, exist_ok=True)
    file_path = os.path.join("uploads", file.filename)  # path used in DB and URL
    full_path = os.path.join(uploads_dir, file.filename)
    with open(full_path, "wb") as f:
        f.write(file.file.read())
    # Record in DB
    db = SessionLocal()
    try:
        img = Image(user_id=0, file_path=file_path)  # user_id placeholder
        db.add(img)
        db.commit()
    finally:
        db.close()
    return RedirectResponse(url="/", status_code=303)
