"""
Abstract base classes for the MVC pattern.

This module defines minimal abstract interfaces that concrete implementations
will inherit from. The goal is to keep the core logic decoupled from
framework‑specific details while still providing a clear contract for
the rest of the application.
"""
from abc import ABC, abstractmethod
from typing import List, Optional

class BaseModel(ABC):
    """Base class for all ORM models."""

    @abstractmethod
    def save(self) -> None:
        """Persist the model instance to the database."""

    @abstractmethod
    def delete(self) -> None:
        """Remove the model instance from the database."""

class UserModel(BaseModel):
    """Abstract interface for user entities."""

    id: int
    email: str
    hashed_password: str

    @abstractmethod
    def verify_password(self, password: str) -> bool:
        """Return True if the provided password matches the stored hash."""

class ImageModel(BaseModel):
    """Abstract interface for uploaded images."""

    id: int
    user_id: int
    file_path: str
    organism_tag: Optional[str]

    @abstractmethod
    def process(self) -> None:
        """Run the image classification pipeline and set ``organism_tag``."""

# Concrete implementations will be provided in app/models_sqlalchemy.py or similar.
