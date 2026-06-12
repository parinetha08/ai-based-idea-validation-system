from fastapi import APIRouter
from app.backend.models.schemas import IdeaRequest
from app.backend.services.idea_analyzer import analyze_idea

router = APIRouter()


@router.post("/validate")
def validate_idea(request: IdeaRequest):
    return analyze_idea(request.idea)
