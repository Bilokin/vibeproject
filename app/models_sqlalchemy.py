"""
SQLAlchemy ORM definitions for the application.

These are concrete implementations of the abstract interfaces defined in
`app.models`. They use a SQLite database by default, but the URL can be
overridden via the ``DATABASE_URL`` environment variable.
"""
import os
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Base class for all models
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    images = relationship("Image", back_populates="user")

class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    file_path = Column(String(255), nullable=False)
    organism_tag = Column(String(255), nullable=True)
    user = relationship("User", back_populates="images")

# Database session factory
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./vibe.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)
