import re

from services.gemini_service import ask_gemini


def extract_ats_score(text):
    """
    Extract ATS score from AI response.

    Supports formats such as:
    ATS Score: 85
    ATS Score: 85/100
    ATS Score - 85
    ATS Score = 85
    """

    if not text:
        return None

    patterns = [
        r"ATS\s*SCORE\s*[:\-=\s]+\**\s*(\d{1,3})\s*(?:/100)?",
        r"ATS\s*Compatibility\s*Score\s*[:\-=\s]+\**\s*(\d{1,3})\s*(?:/100)?",
        r"Overall\s*ATS\s*Score\s*[:\-=\s]+\**\s*(\d{1,3})\s*(?:/100)?",
        r"ATS\s*Rating\s*[:\-=\s]+\**\s*(\d{1,3})\s*(?:/100)?",
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            score = int(match.group(1))

            if 0 <= score <= 100:
                return score

    return None


def analyze_resume(resume_text):

    prompt = f"""
You are an expert ATS resume analyzer and professional technical recruiter.

Analyze the following resume.

IMPORTANT:
Your response MUST start with the ATS score in EXACTLY this format:

ATS Score: XX/100

Replace XX with a number between 0 and 100.

Then provide the complete analysis using the following structure:

## ATS Score
ATS Score: XX/100

## Overall Assessment
Give a short professional summary.

## Key Strengths
- Strength 1
- Strength 2
- Strength 3

## Missing Skills
- Skill 1
- Skill 2
- Skill 3

## Resume Improvements
- Improvement 1
- Improvement 2
- Improvement 3

## ATS Keywords
List important keywords that should be included.

## Recommended Job Roles
List suitable job roles based on the resume.

## Final Recommendations
Give practical steps to improve the resume and ATS compatibility.

Resume:

{resume_text}
"""

    try:

        result = ask_gemini(prompt)

        if not result:
            return "ERROR: AI returned an empty response."

        # Extract ATS score
        ats_score = extract_ats_score(result)

        # Save complete analysis
        import streamlit as st

        st.session_state.resume_analysis = result
        st.session_state.ats_score = ats_score

        return result

    except Exception as e:

        return f"ERROR: {str(e)}"