from services.gemini_service import ask_gemini


def generate_career_advice(
    role,
    company,
    difficulty,
    questions,
    answers,
    evaluations,
    scores
):

    prompt = f"""
You are an expert AI career coach and senior technical interviewer.

Analyze the candidate's complete mock interview performance.

Candidate Target Role:
{role}

Target Company:
{company}

Interview Difficulty:
{difficulty}

Interview Questions:
{questions}

Candidate Answers:
{answers}

AI Evaluations:
{evaluations}

Interview Scores:
{scores}

Based on the candidate's performance, provide personalized career coaching.

Return the response exactly in the following format:

SKILLS TO IMPROVE:
- Skill 1
- Skill 2
- Skill 3

TOPICS TO STUDY:
- Topic 1
- Topic 2
- Topic 3

RECOMMENDED PROJECTS:
- Project 1
- Project 2
- Project 3

INTERVIEW PREPARATION TIPS:
- Tip 1
- Tip 2
- Tip 3

INTERVIEW READINESS:
Give a readiness percentage from 0% to 100% and briefly explain why.

PERSONALIZED CAREER ADVICE:
Give a short personalized paragraph explaining what the candidate should focus on next to improve their chances of getting hired.

Be specific to the candidate's target role and interview performance.
Do not give generic advice.
"""

    return ask_gemini(prompt)