from services.gemini_service import ask_gemini


def evaluate_answer(question, answer):

    prompt = f"""
You are a senior technical interviewer.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Return exactly in this format.

Score: /10

Strengths:
- ...

Weaknesses:
- ...

Ideal Answer:
...

Tips:
- ...
"""

    return ask_gemini(prompt)