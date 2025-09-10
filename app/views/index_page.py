"""
Abstract and concrete classes for the index (gallery) page.

The abstract class defines the contract that any concrete implementation must
provide: rendering a list of images with their organism tags. The concrete
class uses Jinja2 templates to produce an HTML response.
"""
from abc import ABC, abstractmethod
from typing import List, Dict
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

# Abstract interface
class BaseIndexPage(ABC):
    @abstractmethod
    def render(self, images: List[Dict]) -> HTMLResponse:
        """Return an HTML response for the gallery page."""

# Concrete implementation
class IndexPage(BaseIndexPage):
    def __init__(self, template_dir: str | None = None):
        if template_dir is None:
            base = os.path.dirname(os.path.abspath(__file__))
            template_dir = os.path.join(base, "../templates")
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(["html", "xml"]),
        )

    def render(self, images: List[Dict]) -> HTMLResponse:
        template = self.env.get_template("index.html")
        content = template.render(images=images)
        return HTMLResponse(content=content)
