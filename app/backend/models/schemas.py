"""Pydantic schemas for API responses."""

from pydantic import BaseModel


class IdeaRequest(BaseModel):
    """Request schema for idea validation."""

    idea: str


class IdeaResponse(BaseModel):
    """Response schema for idea validation results."""

    score: int
    demand: str
    risks: list[str]
    improvements: list[str]
