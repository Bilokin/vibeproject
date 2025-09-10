from fastapi import APIRouter, Depends, Request, Form
from starlette.responses import RedirectResponse, HTMLResponse
from ..models_sqlalchemy import User  # concrete SQLAlchemy model
from ..controllers import UserController

router = APIRouter()

# Simple in‑memory controller for demo purposes
class DemoUserController(UserController):
    def register(self, email: str, password: str):
        user = User(email=email)
        user.set_password(password)
        user.save()
        return user

    def login(self, email: str, password: str):
        user = User.get_by_email(email)
        if not user or not user.verify_password(password):
            raise Exception("Invalid credentials")
        # In a real app set session/cookie
        return user

controller = DemoUserController()

@router.post("/login")
def login(request: Request, email: str = Form(...), password: str = Form(...)):
    try:
        controller.login(email, password)
    except Exception as e:
        # For simplicity redirect back with error query param
        return RedirectResponse(url="/login?error=1", status_code=303)
    return RedirectResponse(url="/", status_code=303)

# Render login page on GET
@router.get("/login")
def get_login(request: Request):
    # Use Jinja2 template rendering via IndexPage logic but simpler
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    import os
    base = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(base, "../templates")
    env = Environment(loader=FileSystemLoader(template_dir), autoescape=select_autoescape(["html", "xml"]))
    template = env.get_template("login.html")
    content = template.render()
    return HTMLResponse(content=content)