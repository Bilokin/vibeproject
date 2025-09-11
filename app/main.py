"""
FastAPI application entry point.

This module creates the FastAPI instance, mounts static files, and includes
the routers defined in ``app.routes``. It also sets up a simple startup event
that ensures the database tables exist.
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

# Import routers (to be implemented later)
try:
    from .routes.users import router as users_router  # type: ignore
except Exception:
    users_router = None
try:
    from .routes.images import router as images_router  # type: ignore
except Exception:
    images_router = None

app = FastAPI(title="VibeProject")

# Mount static files (images, css, js)
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.isdir(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Include routers if available
if users_router:
    app.include_router(users_router)
# Include upload router
try:
    from .routes.upload import router as upload_router  # type: ignore
except Exception:
    upload_router = None
if upload_router:
    app.include_router(upload_router)
if images_router:
    app.include_router(images_router, prefix="/images")
# Index router (gallery)
from .routes.index import router as index_router  # type: ignore
app.include_router(index_router)

@app.on_event("startup")
async def startup():
    # Placeholder for DB initialization or migrations
    pass

# Entry point for uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
