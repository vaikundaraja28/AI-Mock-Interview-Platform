import streamlit as st

from services.gemini_service import ask_gemini


def analyze_resume(text):

    prompt = f"""
You are an expert HR recruiter.

Analyze this resume.

Return:

1. Summary

2. Skills

3. Strengths

4. Weaknesses

5. Missing Skills

6. ATS Score (/100)

Resume:

{text}
"""

    with st.spinner("Analyzing Resume..."):

        result = ask_gemini(prompt)

    st.markdown(result)