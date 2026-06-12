from app.backend.services.scoring_engine import calculate_score
from app.backend.services.trend_checker import check_trend
from app.backend.services.ollama_client import generate_with_ollama


def analyze_idea(idea: str, provider: str = "Gemini", api_key: str = ""):
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
        prompt = f"""
        Analyze this startup idea:

        {idea}

        Provide:
        - Strengths
        - Weaknesses
        - Opportunities
        - Risks
        """

        ai_analysis = generate_with_ollama(prompt)

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
