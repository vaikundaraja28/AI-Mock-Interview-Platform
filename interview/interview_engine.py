from services.gemini_service import ask_gemini
from interview.prompt import SYSTEM_PROMPT


def generate_question(role, difficulty):

    prompt = f"""
{SYSTEM_PROMPT}

Role:
{role}

Difficulty:
{difficulty}

Generate only ONE interview question.
"""

    return ask_gemini(prompt)