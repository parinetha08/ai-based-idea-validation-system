"""Handles language translation and internationalization utilities."""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]


def load_language(lang):
    """Translate input text into the selected language."""
    file_path = BASE_DIR / "locales" / f"{lang}.json"

    with open(file_path, encoding="utf-8") as f:
        return json.load(f)
