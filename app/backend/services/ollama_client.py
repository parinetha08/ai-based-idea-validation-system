import requests


def generate_with_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3:latest", "prompt": prompt, "stream": False},
        timeout=300,
    )

    response.raise_for_status()

    return response.json()["response"]
