"""Service for checking market trends and relevance of ideas."""


def check_trend(idea: str):
    """Analyze whether an idea is trending in the market."""
    idea = idea.lower()

    if "ai" in idea:
        return "High"

    if "health" in idea or "education" in idea:
        return "Medium"

    return "Low"
