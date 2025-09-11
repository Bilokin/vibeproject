"""
Concrete repository implementation for image persistence.

This module uses SQLAlchemy ORM models (to be defined in ``app/models_sqlalchemy.py``)
and provides a thin data‑access layer that the controllers can use.
"""
from __future__ import annotations

from typing import List, Optional
from sqlalchemy.orm import Session
import app.models_sqlalchemy as ms  # type: ignore
ImageModel = ms.Image

class ImageRepository:
    """Data access object for ``Image`` entities."""

    def __init__(self, db_session: Session):
        self.db = db_session

    def add(self, image: ImageModel) -> None:
        self.db.add(image)
        self.db.commit()
        self.db.refresh(image)

    def get_by_id(self, image_id: int) -> Optional[ImageModel]:
        return self.db.query(ImageModel).filter(ImageModel.id == image_id).first()

    def list_all(self) -> List[ImageModel]:
        return self.db.query(ImageModel).all()

    def list_by_user(self, user_id: int) -> List[ImageModel]:
        return self.db.query(ImageModel).filter(ImageModel.user_id == user_id).all()
