from services.gemini_service import ask_gemini
from interview.prompt import SYSTEM_PROMPT


def generate_question(role, difficulty):

    prompt = f"""
{SYSTEM_PROMPT}

Interview Role:
{role}

Difficulty:
{difficulty}

Generate ONE interview question only.
"""

    return ask_gemini(prompt)