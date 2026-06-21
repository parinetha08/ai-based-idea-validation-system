"""LLM client supporting Ollama, OpenAI, and Gemini."""

import requests

from app.core.config import OPENAI_API_KEY, GEMINI_API_KEY, MODEL_NAME


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
    return response.json()["response"]


# -----------------------------
# OpenAI (placeholder-ready)
# -----------------------------
def generate_with_openai(prompt: str) -> str:
    """Generate response using OpenAI API."""
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is not set")

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        json=payload,
        headers=headers,
        timeout=300,
    )

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


# -----------------------------
# Gemini (placeholder-ready)
# -----------------------------
def generate_with_gemini(prompt: str) -> str:
    """Generate response using Gemini API."""
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not set")

    url = (
        "https://generativelanguage.googleapis.com/v1beta/"
        f"models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
    )

    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    response = requests.post(url, json=payload, timeout=300)
    response.raise_for_status()

    data = response.json()

    return data["candidates"][0]["content"]["parts"][0]["text"]


# -----------------------------
# MAIN ROUTER
# -----------------------------
def generate_response(prompt: str) -> str:
    """
    Main entry point for all LLM calls.
    Chooses model based on MODEL_NAME.
    """

    model = (MODEL_NAME or "ollama").lower()

    if "ollama" in model:
        return generate_with_ollama(prompt)

    if "openai" in model:
        return generate_with_openai(prompt)

    if "gemini" in model:
        return generate_with_gemini(prompt)

    # fallback
    return generate_with_ollama(prompt)
