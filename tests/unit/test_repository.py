import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import importlib.util, os
spec = importlib.util.spec_from_file_location("models_sqlalchemy", os.path.join(os.path.dirname(__file__), "../../app/models_sqlalchemy.py"))
models_sqlalchemy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(models_sqlalchemy)
Base = models_sqlalchemy.Base
Image = models_sqlalchemy.Image
OriginalSessionLocal = models_sqlalchemy.SessionLocal
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from app.repository import ImageRepository

# Use an in‑memory SQLite database for tests
@pytest.fixture(scope="module")
def db_session():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    yield session
    session.close()

@pytest.fixture(scope="module")
def repo(db_session):
    return ImageRepository(db_session)

def test_add_and_get_by_id(repo, db_session):
    img = Image(user_id=1, file_path="/tmp/foo.png", organism_tag="test")
    repo.add(img)
    assert img.id is not None
    fetched = repo.get_by_id(img.id)
    assert fetched is not None
    assert fetched.file_path == "/tmp/foo.png"

def test_list_all(repo, db_session):
    # repository already has one image from previous test
    img2 = Image(user_id=2, file_path="/tmp/bar.png")
    repo.add(img2)
    all_imgs = repo.list_all()
    assert len(all_imgs) == 2

def test_list_by_user(repo, db_session):
    imgs = repo.list_by_user(1)
    assert any(i.user_id == 1 for i in imgs)
