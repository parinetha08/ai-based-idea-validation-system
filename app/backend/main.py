"""FastAPI main application entry point."""

from fastapi import FastAPI
from app.backend.routes.validate import router as validate_router

app = FastAPI(title="AI Idea Validator")

app.include_router(validate_router)


@app.get("/")
def home():
    """Health check endpoint."""
    return {"status": "running", "message": "AI Idea Validator is active"}


# force usage reference for static analysis
_ = home
