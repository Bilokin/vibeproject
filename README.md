# VibeProject

A lightweight web application for microbiologists to upload microscope images, automatically identify microorganisms and tag the images with the detected organism. The app provides a gallery view of all uploaded images along with their tags, and supports user authentication.

## Features
- **User Authentication** – Sign up / log in via email & password.
- **Image Upload** – Users can upload microscope photos from the web interface.
- **Automated Identification** – Images are processed by a pre‑trained model (e.g., a TensorFlow/Keras or PyTorch classifier) that detects and classifies microorganisms. The result is stored as a tag on the image.
- **Gallery Index Page** – Displays all uploaded images in a grid, showing the organism tag in the description.
- **Secure Storage** – Images are stored on disk (or cloud storage if configured) with metadata persisted in a SQLite database.

## Tech Stack
- **Python 3.11+**
- **FastAPI** – Fast, modern web framework for building APIs and serving HTML templates.
- **SQLAlchemy + Alembic** – ORM & migrations for the SQLite database.
- **Jinja2** – Templating engine for rendering the gallery and login pages.
- **Pydantic** – Data validation.
- **Uvicorn** – ASGI server.
- **TensorFlow / PyTorch** – (Optional) For the image classification model.

## Project Structure
```
├── app/                 # FastAPI application code
│   ├── main.py          # Application entry point
│   ├── models.py        # SQLAlchemy ORM models
│   ├── schemas.py       # Pydantic request/response models
│   ├── crud.py          # Database access helpers
│   ├── auth.py          # Authentication utilities (JWT, password hashing)
│   ├── routes/
│   │   ├── users.py    # User registration & login endpoints
│   │   └── images.py   # Image upload & gallery endpoints
│   ├── templates/      # Jinja2 HTML templates
│   │   ├── index.html
│   │   ├── login.html
│   │   └── upload.html
│   └── static/         # CSS, JS, and uploaded images
├── migrations/          # Alembic migration scripts
├── tests/               # Unit & integration tests
└── README.md            # This file
```

## Getting Started
1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd vibeproject
   ```
2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Set up environment variables** – Create a `.env` file (see `.env.example`).
4. **Run database migrations**
   ```bash
   alembic upgrade head
   ```
5. **Start the server**
   ```bash
   uvicorn app.main:app --reload
   ```
6. Open your browser at `http://localhost:8000`.

## Environment Variables (`.env`) Example
```
# Database URL (SQLite by default)
DATABASE_URL=sqlite:///./vibe.db

# Secret key for JWT tokens
SECRET_KEY=super-secret-key

# Password hashing algorithm
HASH_ALGORITHM=bcrypt

# Optional: Path to the pre‑trained model file
MODEL_PATH=models/microbe_classifier.h5
```

## Running Tests
```bash
pytest tests/
```

## Contributing
Pull requests are welcome! Please open an issue first to discuss major changes.

## License
MIT © 2025 VibeProject
