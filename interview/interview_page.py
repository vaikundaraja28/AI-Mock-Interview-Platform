import streamlit as st

from interview.interview_engine import (
    generate_question,
    generate_followup_question
)
from interview.evaluator import evaluate_answer

from history.history_service import save_interview
from utils.score_parser import extract_score
from reports.pdf_report import generate_report

from streamlit_mic_recorder import speech_to_text

def interview_page():

    # -------------------------
    # Initialize Session State
    # -------------------------

    if "current_question" not in st.session_state:
        st.session_state.current_question = 1

    if "total_questions" not in st.session_state:
        st.session_state.total_questions = 5

    if "scores" not in st.session_state:
        st.session_state.scores = []

    if "voice_answer" not in st.session_state:
        st.session_state.voice_answer = ""

    if "followup_question" not in st.session_state:
        st.session_state.followup_question = None

    # -------------------------
    # Page Title
    # -------------------------

    st.title("🎤 AI Mock Interview")

    st.progress(
        st.session_state.current_question
        / st.session_state.total_questions
    )

    st.write(
        f"### Question "
        f"{st.session_state.current_question}"
        f" of "
        f"{st.session_state.total_questions}"
    )

    st.divider()

    # -------------------------
    # Role Selection
    # -------------------------

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

    company = st.selectbox(
        "Target Company",
       [
          "General",
          "Google",
          "Microsoft",
          "Amazon",
          "Meta",
          "Apple",
          "Netflix",
          "TCS",
          "Infosys",
          "Wipro",
          "Accenture",
          "Cognizant",
          "Capgemini"
        ],
        key="company"
    )

    question_count = st.selectbox(
    "Number of Questions",
    [3, 5, 10],
    index=1,
    key="question_count"
    )

    st.divider()

    # -------------------------
    # Generate Question
    # -------------------------

    if st.button(
        "🚀 Generate Question",
        key="generate_question",
        use_container_width=True
    ):
        
        st.session_state.total_questions = question_count
        st.session_state.current_question = 1
        st.session_state.scores = []

        question = generate_question(
            role,
            difficulty,
            st.session_state.get("resume_text")
        )

        if question.startswith("ERROR"):

            st.error(question)

        else:

            st.session_state.question = question

            st.session_state.pop(
                "last_evaluation",
                None
            )

            st.session_state.pop(
                "last_score",
                None
            )

            st.session_state.pop(
                "last_role",
                None
            )

            st.session_state.pop(
                "last_difficulty",
                None
            )

            st.session_state.pop("candidate_answer", None)

            st.rerun()

    # -------------------------
    # Question
    # -------------------------

    if "question" in st.session_state:

        st.subheader("💬 Interview Question")

        st.info(
            st.session_state.question
        )

        answer = st.text_area(
            "Your Answer",
            key="candidate_answer",
            height=200
        )

        # -------------------------
        # Voice Input
        # -------------------------

        st.write("### 🎤 Voice Answer")

        voice_text = speech_to_text(
            language="en",
            start_prompt="🎤 Start Recording",
            stop_prompt="⏹ Stop Recording",
            just_once=True,
            use_container_width=True,
            key="voice_input"
        )

        if voice_text:

            st.session_state.candidate_answer = voice_text
            
            st.rerun()
        # -------------------------
        # Evaluate Answer
        # -------------------------

        if st.button(
            "✅ Evaluate Answer",
            key="evaluate_answer",
            use_container_width=True
        ):

            answer = answer.strip()

            if answer == "":

                st.warning(
                    "Please enter your answer first."
                )

            else:

                with st.spinner(
                    "🤖 AI is evaluating your answer..."
                ):

                    result = evaluate_answer(
                        st.session_state.question,
                        answer
                    )

                    followup_question = generate_followup_question(
                        role=role,
                        difficulty=difficulty,
                        company=company,
                        previous_question=st.session_state.question,
                        candidate_answer=answer
                    )

                    st.session_state.followup_question = followup_question

                    score = extract_score(result)

                score = extract_score(result)

                st.session_state.scores.append(
                    score
                )

                save_interview(
                    user_id=st.session_state.user["id"],
                    role=role,
                    difficulty=difficulty,
                    company=company,
                    question=st.session_state.question,
                    answer=answer,
                    evaluation=result,
                    score=score
                )

                st.session_state.last_evaluation = result
                st.session_state.last_score = score
                st.session_state.last_role = role
                st.session_state.last_difficulty = difficulty

                st.rerun()

        # -------------------------
        # Show Evaluation
        # -------------------------

        if "last_evaluation" in st.session_state:

            st.subheader(
                "📊 AI Evaluation"
            )

            st.markdown(
                st.session_state.last_evaluation
            )
            
            if st.session_state.followup_question:

                st.divider()

                st.subheader("🤖 AI Follow-up Question")

                st.info(st.session_state.followup_question)

                followup_answer = st.text_area(
                "Your Follow-up Answer",
                key="followup_answer",
                height=150
                )

                if st.button(
                   "✅ Evaluate Follow-up",
                   key="evaluate_followup",
                   use_container_width=True
                ):

                   if followup_answer.strip() == "":

                       st.warning(
                       "Please answer the follow-up question."
                       )

                   else:

                     with st.spinner(
                         "🤖 AI is evaluating your follow-up..."
                     ):

                         followup_result = evaluate_answer(
                         st.session_state.followup_question,
                         followup_answer
                         )

                     st.session_state.followup_evaluation = followup_result

                     st.rerun()

                if "followup_evaluation" in st.session_state:

                     st.success("✅ Follow-up Evaluated")

                     st.markdown(
                         st.session_state.followup_evaluation
                     )
                        # -------------------------
            # Next Question
            # -------------------------

            if (
                st.session_state.current_question
                < st.session_state.total_questions
            ):

                if "followup_evaluation" in st.session_state:

                    if st.button(
                        "➡ Next Question",
                        use_container_width=True
                    ):

                        st.session_state.current_question += 1

                        question = generate_question(
                            role,
                            difficulty,
                            company,
                            st.session_state.get(
                                "resume_text"
                            )
                        )

                        if question.startswith("ERROR"):

                            st.error(
                                question
                            )

                        else:

                            st.session_state.question = question

                            st.session_state.pop(
                                "last_evaluation",
                                None
                            )

                            st.session_state.pop(
                                "last_score",
                                None
                            )

                            st.session_state.pop(
                                "followup_question",
                                None
                            )

                            st.session_state.pop(
                                "followup_answer",
                                None
                            )

                            st.session_state.pop(
                                "followup_evaluation",
                                None
                            )

                            st.session_state.pop(
                                "candidate_answer",
                                None
                            )

                            st.session_state.candidate_answer = ""

                            st.session_state.voice_answer = ""

                            st.rerun()

                else:

                    st.info(
                        "Please evaluate the follow-up question before continuing."
                    )


            # -------------------------
            # Interview Completed
            # -------------------------

            else:

                if "followup_evaluation" in st.session_state:

                    st.success(
                        "🎉 Interview Completed!"
                    )

                    average = (
                        sum(
                            st.session_state.scores
                        )
                        /
                        len(
                            st.session_state.scores
                        )
                        if st.session_state.scores
                        else 0
                    )

                    st.metric(
                        "⭐ Final Average Score",
                        f"{average:.1f}/10"
                    )

                    st.divider()

                    # -------------------------
                    # Generate PDF Report
                    # -------------------------

                    if st.button(
                        "📄 Generate PDF Report",
                        use_container_width=True
                    ):

                        filename = "Interview_Report.pdf"

                        generate_report(
                            filename=filename,
                            user=st.session_state.user["name"],
                            role=st.session_state.last_role,
                            difficulty=st.session_state.last_difficulty,
                            company=company,
                            question=st.session_state.question,
                            answer=st.session_state.candidate_answer,
                            evaluation=st.session_state.last_evaluation,
                            overall_score=average,
                            followup_question=st.session_state.followup_question,
                            followup_answer=st.session_state.get(
                                "followup_answer",
                                "Not Available"
                            ),
                            followup_evaluation=st.session_state.get(
                                "followup_evaluation",
                                "Not Available"
                            )
                        )

                        st.success(
                            "✅ PDF report generated successfully!"
                        )

                        with open(
                            filename,
                            "rb"
                        ) as pdf:

                            st.download_button(
                                "⬇ Download Interview Report",
                                data=pdf,
                                file_name=filename,
                                mime="application/pdf",
                                use_container_width=True
                            )

                    # -------------------------
                    # Finish Interview
                    # -------------------------

                    if st.button(
                        "🏠 Finish Interview",
                        use_container_width=True
                    ):

                        st.session_state.current_question = 1

                        st.session_state.scores = []

                        st.session_state.voice_answer = ""

                        st.session_state.pop(
                            "question",
                            None
                        )

                        st.session_state.pop(
                            "candidate_answer",
                            None
                        )

                        st.session_state.pop(
                            "last_evaluation",
                            None
                        )

                        st.session_state.pop(
                            "last_score",
                            None
                        )

                        st.session_state.pop(
                            "last_role",
                            None
                        )

                        st.session_state.pop(
                            "last_difficulty",
                            None
                        )

                        st.session_state.pop(
                            "followup_question",
                            None
                        )

                        st.session_state.pop(
                            "followup_answer",
                            None
                        )

                        st.session_state.pop(
                            "followup_evaluation",
                            None
                        )

                        st.session_state.page = "dashboard"

                        st.rerun()

                else:

                    st.info(
                        "Please evaluate the follow-up question to complete the interview."
                    )