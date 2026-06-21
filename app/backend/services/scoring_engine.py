"""Scoring engine for idea evaluation."""

from app.core.constants import MAX_SCORE
from app.utils.text_processing import word_count


def calculate_score(idea: str) -> int:
    """
    Calculate a basic heuristic score for an idea.

    Scoring is based on idea length (can be replaced later with AI scoring).
    """

    length = word_count(idea)

    if length < 30:
        score = 60
    elif length < 100:
        score = 75
    else:
        score = 85

    # Ensure score never exceeds MAX_SCORE (fixes vulture + future safety)
    return min(score, MAX_SCORE)
