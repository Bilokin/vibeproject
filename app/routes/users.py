from fastapi import APIRouter, Request, Form
from starlette.responses import RedirectResponse, HTMLResponse
from ..models_sqlalchemy import User
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

router = APIRouter()

@router.get("/login")
def get_login(request: Request):
    base = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(base, "../templates")
    env = Environment(loader=FileSystemLoader(template_dir), autoescape=select_autoescape(["html", "xml"]))
    template = env.get_template("login.html")
    return HTMLResponse(content=template.render())

@router.post("/login")
def post_login(email: str = Form(...), password: str = Form(...)):
    user = User.get_by_email(email)
    if not user or not user.verify_password(password):
        return RedirectResponse(url="/login?error=1", status_code=303)
    return RedirectResponse(url="/", status_code=303)

@router.post("/register")
def post_register(email: str = Form(...), password: str = Form(...)):
    # Simple duplicate check
    if User.get_by_email(email):
        return RedirectResponse(url="/login?error=2", status_code=303)
    user = User(email=email)
    user.set_password(password)
    from ..models_sqlalchemy import SessionLocal
    db = SessionLocal()
    try:
        db.add(user)
        db.commit()
    finally:
        db.close()
    # Mock email verification step
    return RedirectResponse(url="/login?registered=1", status_code=303)
