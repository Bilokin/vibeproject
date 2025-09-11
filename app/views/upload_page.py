from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

class UploadPage:
    def __init__(self):
        base = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(base, "../templates")
        self.env = Environment(loader=FileSystemLoader(template_dir), autoescape=select_autoescape(["html", "xml"]))

    def render(self) -> str:
        template = self.env.get_template("upload.html")
        return template.render()
