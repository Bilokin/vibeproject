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
