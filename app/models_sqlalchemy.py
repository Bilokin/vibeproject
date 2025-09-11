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

    def set_password(self, password: str):
        import bcrypt
        self.hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify_password(self, password: str) -> bool:
        import bcrypt
        return bcrypt.checkpw(password.encode(), self.hashed_password.encode())

    @classmethod
    def get_by_email(cls, email: str):
        session = SessionLocal()
        try:
            return session.query(cls).filter_by(email=email).first()
        finally:
            session.close()

    # Simple password handling
    def set_password(self, raw: str):
        import hashlib
        self.hashed_password = hashlib.sha256(raw.encode()).hexdigest()

    def verify_password(self, raw: str) -> bool:
        import hashlib
        return self.hashed_password == hashlib.sha256(raw.encode()).hexdigest()

    @classmethod
    def get_by_email(cls, email: str):
        session = SessionLocal()
        try:
            return session.query(cls).filter_by(email=email).first()
        finally:
            session.close()

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
