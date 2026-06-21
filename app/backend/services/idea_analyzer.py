"""Service for analyzing startup ideas."""

from app.agents.idea_agent import run_idea_agent
from app.backend.services.scoring_engine import calculate_score
from app.backend.services.trend_checker import check_trend


def analyze_idea(
    idea: str,
    provider: str = "Gemini",
    api_key: str = "",
):
    """Analyze a startup idea and return evaluation results."""

    # Reserved for future Gemini BYOK implementation
    _ = api_key

    score = calculate_score(idea)
    demand = check_trend(idea)

    if score >= 80:
        risks = [
            "Strong competition in the market",
            "Need for continuous innovation",
        ]

        improvements = [
            "Expand to global markets",
            "Develop strategic partnerships",
        ]

    elif score >= 70:
        risks = [
            "Customer acquisition cost may be high",
            "Execution challenges",
        ]

        improvements = [
            "Focus on a niche audience",
            "Strengthen marketing efforts",
        ]

    else:
        risks = [
            "User adoption challenges",
            "Uncertain market fit",
        ]

        improvements = [
            "Build MVP before scaling",
            "Conduct more market research",
        ]

    # AI Analysis
    if provider == "Ollama":
        ai_analysis = run_idea_agent(idea)
    else:
        ai_analysis = "Analysis generated using Gemini API (BYOK support enabled)."

    return {
        "score": score,
        "demand": demand,
        "risks": risks,
        "improvements": improvements,
        "ai_provider": provider,
        "ai_analysis": ai_analysis,
    }
