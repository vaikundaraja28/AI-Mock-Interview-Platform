import streamlit as st

from interview.interview_engine import generate_question
from interview.evaluator import evaluate_answer

from history.history_service import save_interview
from utils.score_parser import extract_score


def interview_page():

    st.title("🎤 AI Mock Interview")

    role = st.selectbox(
        "Choose Job Role",
        [
            "Python Developer",
            "Java Developer",
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Developer",
            "Data Analyst",
            "Machine Learning Engineer"
        ],
        key="role"
    )

    difficulty = st.selectbox(
        "Choose Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ],
        key="difficulty"
    )

    st.divider()

    if st.button(
        "🚀 Generate Question",
        key="generate_question",
        use_container_width=True
    ):

        question = generate_question(role, difficulty)

        if question.startswith("ERROR"):

            st.error(question)

        else:

            st.session_state.question = question
            st.session_state.candidate_answer = ""

            st.rerun()

    if "question" in st.session_state:

        st.subheader("💬 Interview Question")

        st.info(st.session_state.question)

        st.text_area(
            "Your Answer",
            key="candidate_answer",
            height=200
        )

        if st.button(
            "✅ Evaluate Answer",
            key="evaluate_answer",
            use_container_width=True
        ):

            answer = st.session_state.candidate_answer.strip()

            if answer == "":

                st.warning("Please enter your answer first.")

            else:

                with st.spinner("🤖 AI is evaluating your answer..."):

                    result = evaluate_answer(
                        st.session_state.question,
                        answer
                    )

                score = extract_score(result)

                save_interview(
                    user_id=st.session_state.user["id"],
                    role=role,
                    difficulty=difficulty,
                    question=st.session_state.question,
                    answer=answer,
                    evaluation=result,
                    score=score
                )

                st.subheader("📊 AI Evaluation")

                st.markdown(result)