def check_trend(idea: str):
    idea = idea.lower()

    if "ai" in idea:
        return "High"
    elif "health" in idea or "education" in idea:
        return "Medium"
    else:
        return "Low"
