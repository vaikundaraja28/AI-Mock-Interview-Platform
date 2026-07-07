import streamlit as st


def hero():

    st.markdown(
        """
        <div style="text-align:center;padding:20px 0 50px 0;">

        <h1 style="
        font-size:72px;
        color:white;
        margin-bottom:10px;">

        🤖 AI Mock Interview

        </h1>

        <h3 style="color:#9CA3AF;">

        Master Your Dream Job

        </h3>

        <p style="
        color:#94A3B8;
        font-size:22px;
        max-width:700px;
        margin:auto;">

        Practice Technical, HR and Aptitude interviews using
        Google's Gemini AI.
        Receive instant scoring,
        communication analysis,
        resume review
        and personalized feedback.

        </p>

        </div>
        """,
        unsafe_allow_html=True
    )