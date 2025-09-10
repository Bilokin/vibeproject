"""
Abstract view layer for rendering templates or JSON responses.

In a FastAPI application the concrete views will be simple functions that
return either ``HTMLResponse`` or ``JSONResponse``. These abstract classes
serve only as documentation of the expected interface.
"""
from abc import ABC, abstractmethod
from typing import Any

class BaseView(ABC):
    """Base class for all view handlers."""

    @abstractmethod
    def render(self, context: dict) -> Any:
        ...

class IndexView(BaseView):
    """Render the gallery index page."""

    @abstractmethod
    def render(self, images: list[dict]) -> Any:
        ...

class LoginView(BaseView):
    """Render the login form or return a redirect after successful auth."""

    @abstractmethod
    def render(self, error: str | None = None) -> Any:
        ...
