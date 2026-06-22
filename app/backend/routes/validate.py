"""API routes for idea validation."""

from fastapi import APIRouter

from app.backend.models.schemas import IdeaRequest, IdeaResponse
from app.agents.idea_agent import run_idea_agent
from app.utils.helpers import clean_text

router = APIRouter()


@router.post("/validate", response_model=IdeaResponse)
def validate_idea(request: IdeaRequest) -> IdeaResponse:
    """Validate a startup idea using the AI pipeline."""

    cleaned_idea = clean_text(request.idea)

    result = run_idea_agent(cleaned_idea)

    return IdeaResponse(
        score=0,
        demand=result,
        risks=[],
        improvements=[],
    )
