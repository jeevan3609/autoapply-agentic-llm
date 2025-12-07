import os
import requests
from textwrap import shorten

# If True => no real API calls, just previews
DUMMY_MODE = False

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.1-8b-instant"


def _get_groq_headers() -> dict:
    """Build headers for Groq Chat Completions API."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. In this terminal run:\n"
            "  set GROQ_API_KEY=your_key_here"
        )
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }


def call_llm(system_prompt: str, user_prompt: str, temperature: float = 0.2) -> str:
    """
    Shared LLM caller for all agents.

    - In DUMMY_MODE: returns a fake preview string (no API calls).
    - In real mode: sends a Chat Completions request to Groq.
    """
    if DUMMY_MODE:
        sys_preview = shorten(system_prompt.replace("\n", " "), width=80)
        usr_preview = shorten(user_prompt.replace("\n", " "), width=80)
        return (
            "DUMMY_LLM_RESPONSE\n\n"
            f"[system_prompt_preview]: {sys_preview}\n"
            f"[user_prompt_preview]: {usr_preview}\n\n"
            "Note: DUMMY_MODE is ON. No real reasoning performed."
        )

    payload = {
        "model": GROQ_MODEL,
        "temperature": temperature,
        "max_tokens": 512,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }

    response = requests.post(
        GROQ_API_URL,
        headers=_get_groq_headers(),
        json=payload,
        timeout=60,
    )
    response.raise_for_status()
    data = response.json()

    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        return str(data)
