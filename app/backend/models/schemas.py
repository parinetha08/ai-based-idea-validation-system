from pydantic import BaseModel


class IdeaRequest(BaseModel):
    idea: str


class IdeaResponse(BaseModel):
    score: int
    demand: str
    risks: list[str]
    improvements: list[str]
