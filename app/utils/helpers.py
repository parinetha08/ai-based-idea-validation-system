"""General helper utilities used across the application."""


def clean_text(text: str) -> str:
    """Normalize input text by stripping whitespace and converting to lowercase."""
    return text.strip().lower()
