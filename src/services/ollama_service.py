import requests
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL


def generate_text(prompt, temperature=0.7, top_p=0.9):
    """
    Send prompt to Ollama LLM and return generated text
    """

    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "temperature": temperature,
            "top_p": top_p,
            "stream": False
        }
    )

    return response.json()["response"]