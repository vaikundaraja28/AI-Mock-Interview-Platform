import streamlit as st

from interview.interview_engine import generate_question


def interview_page():

    st.title("🎤 AI Mock Interview")

    role = st.selectbox(
        "Choose Role",
        [
            "Python Developer",
            "Java Developer",
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Developer",
            "Data Analyst",
            "Machine Learning Engineer"
        ]
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    st.divider()

    if st.button(
        "🚀 Start Interview",
        use_container_width=True
    ):

        question = generate_question(
            role,
            difficulty
        )

        st.session_state.question = question

    if "question" in st.session_state:

        st.success("Question Generated")

        st.markdown("### 💬 Interview Question")

        st.info(st.session_state.question)

        answer = st.text_area(
            "Your Answer",
            height=250
        )

        if st.button(
            "Submit Answer",
            use_container_width=True
        ):

            st.success("Answer submitted!")

            st.info(
                "AI Evaluation will be added in the next phase."
            )