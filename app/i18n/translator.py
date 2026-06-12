import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

def load_language(lang):
    file_path = BASE_DIR / "locales" / f"{lang}.json"

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)