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