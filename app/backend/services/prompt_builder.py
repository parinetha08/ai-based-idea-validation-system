"""Prompt builder for idea validation."""


def build_prompt(idea: str) -> str:
    """
    Builds structured prompt for LLM-based idea evaluation.
    """

    return f"""
You are an expert startup mentor and analyst.

Analyze the following startup idea step by step:

Idea:
{idea}

Return your response in the following format:

1. Score (0-100)
2. Market Demand (Low / Medium / High)
3. Risks (bullet points)
4. Improvements (bullet points)
5. Final Verdict (1-2 lines)
"""
