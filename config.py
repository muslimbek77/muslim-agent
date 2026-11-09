import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL = "claude-haiku-5-5"
MAX_TOKENS = 1024


def require_api_key():
    """Ensure the Anthropic API key is available before starting the agent."""
    if not API_KEY:
        raise ValueError(
            "ANTHROPIC_API_KEY topilmadi. .env faylida yoki terminal environmentida qo'ying."
        )
    return API_KEY
