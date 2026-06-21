"""Handles parsing and processing of AI model outputs."""


def parse_output(data):
    """Parse raw AI output into structured data."""
    return {
        "score": data.get("score"),
        "demand": data.get("demand"),
        "risks": data.get("risks"),
        "improvements": data.get("improvements"),
    }
