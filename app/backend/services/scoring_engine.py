def calculate_score(idea: str) -> int:
    length = len(idea)

    if length < 30:
        return 60
    elif length < 100:
        return 75
    else:
        return 85