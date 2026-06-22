"""LLM client supporting Ollama, OpenAI, and Gemini."""

from typing import Any

import requests

from app.core.config import GEMINI_API_KEY, MODEL_NAME, OPENAI_API_KEY


# -----------------------------
# Ollama
# -----------------------------
def generate_with_ollama(prompt: str) -> str:
    """Generate response using local Ollama model."""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3:latest",
            "prompt": prompt,
            "stream": False,
        },
        timeout=300,
    )

    response.raise_for_status()

    data: dict[str, Any] = response.json()
    return str(data["response"])


# -----------------------------
# OpenAI
# -----------------------------
def generate_with_openai(prompt: str) -> str:
    """Generate response using OpenAI API."""

    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is not set")

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }

    payload: dict[str, Any] = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        json=payload,
        headers=headers,
        timeout=300,
    )

    response.raise_for_status()

    data: dict[str, Any] = response.json()
    return str(data["choices"][0]["message"]["content"])


# -----------------------------
# Gemini
# -----------------------------
def generate_with_gemini(
    prompt: str,
    api_key: str = "",
) -> str:
    """Generate response using Gemini API."""

    key = api_key or GEMINI_API_KEY

    if not key:
        raise ValueError("Gemini API key is required")

    url = (
        "https://generativelanguage.googleapis.com/v1beta/"
        f"models/gemini-2.5-flash:generateContent?key={key}"
    )

    payload: dict[str, Any] = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt,
                    }
                ]
            }
        ]
    }

    response = requests.post(
        url,
        json=payload,
        timeout=300,
    )

    response.raise_for_status()

    data: dict[str, Any] = response.json()

    return str(data["candidates"][0]["content"]["parts"][0]["text"])


# -----------------------------
# MAIN ROUTER
# -----------------------------
def generate_response(
    prompt: str,
    provider: str = "",
    api_key: str = "",
) -> str:
    """Route request to selected provider."""

    selected_provider = provider.lower()

    if selected_provider == "gemini":
        return generate_with_gemini(
            prompt=prompt,
            api_key=api_key,
        )

    if selected_provider == "ollama":
        return generate_with_ollama(prompt)

    model = (MODEL_NAME or "ollama").lower()

    if "gemini" in model:
        return generate_with_gemini(
            prompt=prompt,
            api_key=api_key,
        )

    if "openai" in model:
        return generate_with_openai(prompt)

    return generate_with_ollama(prompt)
