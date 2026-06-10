def parse_output(data):
    return {
        "score": data.get("score"),
        "demand": data.get("demand"),
        "risks": data.get("risks"),
        "improvements": data.get("improvements")
    }