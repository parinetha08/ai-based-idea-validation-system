def check_trend(idea: str) -> str:
    keywords = ["ai", "automation", "startup", "health", "education"]

    for word in keywords:
        if word.lower() in idea.lower():
            return "High"

    return "Medium"
