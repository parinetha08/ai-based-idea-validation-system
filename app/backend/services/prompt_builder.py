def build_prompt(idea: str) -> str:
    return f"""
    Evaluate this startup idea:

    {idea}

    Return:
    - Score
    - Market Demand
    - Risks
    - Improvements
    """