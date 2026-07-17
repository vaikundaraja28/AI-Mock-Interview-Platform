from services.gemini_service import ask_gemini
from interview.prompt import SYSTEM_PROMPT


def generate_question(role, difficulty,company, resume_text=None):

    if resume_text:

        prompt = f"""
{SYSTEM_PROMPT}

You are a senior technical interviewer.

Candidate is applying for:

{role}

Target Company:

{company}

Difficulty:

{difficulty}
=========================
CANDIDATE RESUME
=========================

{resume_text}

=========================
IMPORTANT INSTRUCTIONS
=========================

Generate EXACTLY ONE interview question.

The question MUST be based on the candidate's resume.

Priority order:

1. Projects
2. Internship
3. Technical Skills
4. Certifications
5. Education

DO NOT ask generic programming questions unless none of the above exist.

Examples of good questions:

- Explain the architecture of your Patient Health Monitoring System.
- Why did you use Arduino Uno in your IoT project?
- During your Emglitz internship, what did you learn?
- Explain the communication protocol used in your Home Automation project.
- Which part of your project was the most challenging?

Return ONLY the question.
"""

    else:

     prompt = f"""
     {SYSTEM_PROMPT}

     You are an experienced technical interviewer.

     Target Company:
     {company}

     Candidate Role:
     {role}

     Difficulty:
     {difficulty}

     Generate EXACTLY ONE interview question.

     If the company is General, generate a normal interview question.

     Otherwise, generate a question that matches the interview style of {company}.

     Return ONLY the question.
     """

    return ask_gemini(prompt)

def generate_followup_question(
    role,
    difficulty,
    company,
    previous_question,
    candidate_answer
):
    prompt = f"""
{SYSTEM_PROMPT}

You are an experienced technical interviewer.

Role:
{role}

Company:
{company}

Difficulty:
{difficulty}

Previous Question:
{previous_question}

Candidate Answer:
{candidate_answer}

Your task:

Generate ONE natural follow-up interview question based ONLY on the candidate's previous answer.

Rules:

- Ask only ONE question.
- It must relate directly to the candidate's answer.
- Make it feel like a real interviewer continuing the conversation.
- Do NOT repeat the previous question.
- Do NOT change the topic completely.
- Return ONLY the follow-up question.
"""

    return ask_gemini(prompt)