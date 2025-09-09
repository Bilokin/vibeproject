"""
Abstract base classes for MVC controllers.

Concrete controllers will implement the HTTP request handling logic and
delegate business operations to services or models defined elsewhere.
"""
from abc import ABC, abstractmethod
from typing import Any

class BaseController(ABC):
    """Base class for all controllers."""

    @abstractmethod
    def get(self, *args: Any, **kwargs: Any) -> Any:
        ...

    @abstractmethod
    def post(self, *args: Any, **kwargs: Any) -> Any:
        ...

class UserController(BaseController):
    """Abstract interface for user‑related endpoints."""

    @abstractmethod
    def register(self, email: str, password: str) -> Any:
        ...

    @abstractmethod
    def login(self, email: str, password: str) -> Any:
        ...

class ImageController(BaseController):
    """Abstract interface for image upload and gallery endpoints."""

    @abstractmethod
    def upload(self, user_id: int, file_data: bytes, filename: str) -> Any:
        ...

    @abstractmethod
    def list_images(self, user_id: Optional[int] = None) -> Any:
        ...
