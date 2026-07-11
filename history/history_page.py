import streamlit as st

from history.history_service import get_history, get_interview


def history_page():

    st.title("📜 Interview History")

    history = get_history(
        st.session_state.user["id"]
    )

    if len(history) == 0:

        st.info("You haven't taken any interviews yet.")
        return

    for interview in history:

        interview_id = interview[0]
        role = interview[1]
        difficulty = interview[2]
        score = interview[3]
        date = interview[4]

        with st.expander(
            f"{role} | {difficulty} | ⭐ {score}/10"
        ):

            question, answer, evaluation = get_interview(interview_id)

            st.write(f"**Interview ID:** {interview_id}")
            st.write(f"**Role:** {role}")
            st.write(f"**Difficulty:** {difficulty}")
            st.write(f"**Score:** {score}/10")
            st.write(f"**Date:** {date}")

            st.divider()

            st.subheader("📄 Interview Question")
            st.info(question)

            st.subheader("💬 Your Answer")
            st.write(answer)

            st.subheader("🤖 AI Evaluation")
            st.markdown(evaluation)