from app.backend.services.scoring_engine import calculate_score
from app.backend.services.trend_checker import check_trend


def analyze_idea(idea: str):
    score = calculate_score(idea)
    demand = check_trend(idea)

    return {
        "score": score,
        "demand": demand,
        "risks": ["Competition from existing products", "User adoption challenges"],
        "improvements": [
            "Focus on a specific target audience",
            "Build MVP before scaling",
        ],
    }
