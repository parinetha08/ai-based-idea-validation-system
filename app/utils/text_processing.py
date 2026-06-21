"""Text preprocessing utilities for NLP tasks."""


def word_count(text: str) -> int:
    """Preprocess text by removing noise and normalizing content."""
    return len(text.split())
