import streamlit as st

from interview.interview_engine import (
    generate_question,
    generate_followup_question
)

from interview.evaluator import (
    evaluate_answer
)

from history.history_service import (
    save_interview
)

from utils.score_parser import (
    extract_score
)

from reports.pdf_report import (
    generate_report
)

from services.career_coach import (
    generate_career_advice
)

from streamlit_mic_recorder import (
    speech_to_text
)


# =========================================================
# HELPER
# =========================================================

def md(html: str):
    """
    Render HTML safely.
    Each line is stripped individually to avoid
    Streamlit interpreting indented HTML as code.
    """

    lines = [
        line.strip()
        for line in html.strip("\n").splitlines()
    ]

    st.markdown(
        "\n".join(lines),
        unsafe_allow_html=True
    )


# =========================================================
# INITIALIZE SESSION STATE
# =========================================================

def initialize_interview_state():

    defaults = {
        "current_question": 1,
        "total_questions": 3,
        "scores": [],
        "voice_answer": "",
        "followup_question": None,
        "interview_questions": [],
        "interview_answers": [],
        "interview_evaluations": [],
    }

    for key, value in defaults.items():

        if key not in st.session_state:

            # Use copy for lists
            if isinstance(value, list):
                st.session_state[key] = value.copy()

            else:
                st.session_state[key] = value


# =========================================================
# STYLES
# =========================================================

def load_interview_styles():

    md("""
    <style>

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* HEADER */

    .interview-header {
        margin-bottom: 1.5rem;
    }

    .interview-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #F8FAFC;
        line-height: 1.2;
        margin-bottom: 0.4rem;
    }

    .interview-subtitle {
        font-size: 0.95rem;
        color: #94A3B8;
        line-height: 1.5;
    }

    /* PROGRESS */

    .progress-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.4rem;
    }

    .progress-title {
        font-size: 0.9rem;
        font-weight: 600;
        color: #CBD5E1;
    }

    .progress-count {
        font-size: 0.85rem;
        font-weight: 700;
        color: #8EA8FF;
    }

    .stProgress {
        margin-top: 0 !important;
        margin-bottom: 1.5rem !important;
    }

    /* SECTION TITLES */

    .section-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-top: 0.5rem;
        margin-bottom: 0.25rem;
    }

    .section-subtitle {
        font-size: 0.9rem;
        color: #94A3B8;
        margin-bottom: 1rem;
    }

    /* QUESTION CARD */

    .question-card {
        background: linear-gradient(
            145deg,
            #111827,
            #0F172A
        );

        border: 1px solid #25304A;

        border-radius: 16px;

        padding: 24px;

        margin-top: 1.5rem;

        margin-bottom: 1.25rem;

        box-shadow:
            0 12px 30px rgba(0,0,0,0.18);
    }

    .question-label {
        color: #8EA8FF;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.65rem;
    }

    .question-text {
        color: #F8FAFC;
        font-size: 1.15rem;
        font-weight: 600;
        line-height: 1.6;
    }

    /* SELECTBOX */

    .stSelectbox label {
        color: #CBD5E1 !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
    }

    /* TEXT AREA */

    .stTextArea {
        margin-top: 0.5rem;
    }

    .stTextArea textarea {
        background: #0B1222 !important;
        color: #F8FAFC !important;

        border: 1px solid #25304A !important;

        border-radius: 10px !important;

        font-size: 0.95rem !important;

        line-height: 1.6 !important;
    }

    .stTextArea textarea:focus {
        border-color: #4F7CFF !important;

        box-shadow:
            0 0 0 2px
            rgba(79,124,255,0.15) !important;
    }

    /* BUTTONS */

    .stButton {
        margin-top: 0.5rem;
    }

    .stButton > button {
        height: 46px;

        border-radius: 10px;

        border: none;

        font-weight: 700;

        background:
            linear-gradient(
                135deg,
                #4F7CFF,
                #635BFF
            );

        color: white;

        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-1px);

        box-shadow:
            0 8px 20px
            rgba(79,124,255,0.25);
    }

    /* DIVIDERS */

    hr {
        margin-top: 1.5rem !important;
        margin-bottom: 1.5rem !important;
    }

    /* MOBILE */

    @media (max-width: 768px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .interview-title {
            font-size: 1.8rem;
        }

        .question-text {
            font-size: 1rem;
        }

        .question-card {
            padding: 18px;
        }

    }

    </style>
    """)


# =========================================================
# INTERVIEW SETUP
# =========================================================

def render_interview_setup():

    # HEADER

    md("""
    <div class="interview-header">

        <div class="interview-title">
            🎤 AI Mock Interview
        </div>

        <div class="interview-subtitle">
            Practice real-world interviews with AI-powered
            questions and personalized feedback.
        </div>

    </div>
    """)

    # PROGRESS

    progress = (
        st.session_state.current_question
        /
        st.session_state.total_questions
    )

    md(f"""
    <div class="progress-header">

        <span class="progress-title">
            Interview Progress
        </span>

        <span class="progress-count">
            Question
            {st.session_state.current_question}
            /
            {st.session_state.total_questions}
        </span>

    </div>
    """)

    st.progress(
        min(progress, 1.0)
    )

    # SETUP TITLE

    md("""
    <div class="section-title">
        ⚙️ Interview Setup
    </div>

    <div class="section-subtitle">
        Customize your interview before you begin.
    </div>
    """)

    # SETUP FIELDS

    col1, col2 = st.columns(
        2,
        gap="large"
    )

    with col1:

        role = st.selectbox(
            "💼 Job Role",
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

        company = st.selectbox(
            "🏢 Target Company",
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

    with col2:

        difficulty = st.selectbox(
            "🎯 Difficulty",
            [
                "Easy",
                "Medium",
                "Hard"
            ],
            key="difficulty"
        )

        question_count = st.selectbox(
            "🔢 Number of Questions",
            [
                1,
                3,
                5,
                10
            ],
            index=1,
            key="question_count"
        )

    md(
        "<div style='height: 8px'></div>"
    )

    # START INTERVIEW

    if st.button(
        "🚀 Start AI Interview",
        key="generate_question",
        use_container_width=True
    ):

        # Reset interview data

        st.session_state.total_questions = (
            question_count
        )

        st.session_state.current_question = 1

        st.session_state.scores = []

        st.session_state.interview_questions = []

        st.session_state.interview_answers = []

        st.session_state.interview_evaluations = []

        st.session_state.voice_answer = ""

        # IMPORTANT:
        # Do NOT pop candidate_answer here.
        #
        # Instead, use a dynamic widget key
        # based on interview question number.

        question = generate_question(
            role,
            difficulty,
            company,
            st.session_state.get(
                "resume_text"
            )
        )

        if question.startswith("ERROR"):

            st.error(question)

        else:

            st.session_state.question = (
                question
            )

            # Clear previous evaluation state

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
                "followup_evaluation",
                None
            )

            st.rerun()

    return (
        role,
        difficulty,
        company,
        question_count
    )


# =========================================================
# QUESTION SECTION
# =========================================================

def render_question_section(
    role,
    difficulty,
    company
):

    if "question" not in st.session_state:

        return

    # -----------------------------------------------------
    # CREATE UNIQUE WIDGET KEY
    # -----------------------------------------------------

    # This is the most important fix.
    #
    # Instead of always using:
    #
    # candidate_answer
    #
    # we use:
    #
    # candidate_answer_1
    # candidate_answer_2
    # candidate_answer_3
    #
    # Therefore, Streamlit never has to modify
    # an existing widget's session state.

    answer_key = (
        f"candidate_answer_"
        f"{st.session_state.current_question}"
    )

    # -----------------------------------------------------
    # QUESTION CARD
    # -----------------------------------------------------

    question_html = (
        st.session_state.question
        .replace(
            "\n",
            "<br>"
        )
    )

    md(
        f"""
        <div class="question-card">

            <div class="question-label">
                Question
                {st.session_state.current_question}
            </div>

            <div class="question-text">
                {question_html}
            </div>

        </div>
        """
    )

    # -----------------------------------------------------
    # VOICE INPUT
    # -----------------------------------------------------

    st.markdown(
        "### 🎤 Voice Answer"
    )

    voice_text = speech_to_text(
        language="en",

        start_prompt=
            "🎤 Start Recording",

        stop_prompt=
            "⏹ Stop Recording",

        just_once=True,

        use_container_width=True,

        key=(
            f"voice_input_"
            f"{st.session_state.current_question}"
        )
    )

    # IMPORTANT:
    #
    # We DO NOT do:
    #
    # st.session_state[answer_key] = voice_text
    #
    # because the text_area may already exist
    # in the current Streamlit execution.
    #
    # Instead we store voice text separately.

    if voice_text:

        st.session_state.voice_answer = (
            voice_text
        )

        st.success(
            "🎤 Voice answer recorded successfully."
        )

    # -----------------------------------------------------
    # TEXT ANSWER
    # -----------------------------------------------------

    typed_answer = st.text_area(
        "✍️ Your Answer",

        key=answer_key,

        height=200,

        placeholder=
            "Type your answer here..."
    )

    # -----------------------------------------------------
    # SHOW VOICE ANSWER
    # -----------------------------------------------------

    if st.session_state.get(
        "voice_answer",
        ""
    ).strip():

        st.info(
            "🎤 Voice answer is ready "
            "and will be used for evaluation."
        )

    # -----------------------------------------------------
    # EVALUATE
    # -----------------------------------------------------

    if st.button(
        "✅ Evaluate Answer",

        key="evaluate_answer",

        use_container_width=True
    ):

        # Get typed answer

        typed_answer = (
            st.session_state
            .get(
                answer_key,
                ""
            )
            .strip()
        )

        # Get voice answer

        voice_answer = (
            st.session_state
            .get(
                "voice_answer",
                ""
            )
            .strip()
        )

        # Voice has priority

        if voice_answer:

            answer = voice_answer

        else:

            answer = typed_answer

        # -------------------------------------------------
        # VALIDATE
        # -------------------------------------------------

        if not answer:

            st.warning(
                "Please type an answer "
                "or record a voice answer first."
            )

            return

        # -------------------------------------------------
        # AI EVALUATION
        # -------------------------------------------------

        with st.spinner(
            "🤖 AI is evaluating your answer..."
        ):

            result = evaluate_answer(
                st.session_state.question,
                answer
            )

            followup_question = (
                generate_followup_question(
                    role=role,
                    difficulty=difficulty,
                    company=company,
                    previous_question=
                        st.session_state.question,
                    candidate_answer=
                        answer
                )
            )

        # -------------------------------------------------
        # EXTRACT SCORE
        # -------------------------------------------------

        score = extract_score(
            result
        )

        # -------------------------------------------------
        # SAVE INTERVIEW STATE
        # -------------------------------------------------

        st.session_state.followup_question = (
            followup_question
        )

        st.session_state.scores.append(
            score
        )

        st.session_state.interview_questions.append(
            st.session_state.question
        )

        st.session_state.interview_answers.append(
            answer
        )

        st.session_state.interview_evaluations.append(
            result
        )

        # -------------------------------------------------
        # SAVE TO DATABASE
        # -------------------------------------------------

        save_interview(

            user_id=
                st.session_state.user["id"],

            role=role,

            difficulty=difficulty,

            company=company,

            question=
                st.session_state.question,

            answer=answer,

            evaluation=result,

            score=score
        )

        # -------------------------------------------------
        # SAVE EVALUATION
        # -------------------------------------------------

        st.session_state.last_evaluation = (
            result
        )

        st.session_state.last_score = (
            score
        )

        st.session_state.last_role = (
            role
        )

        st.session_state.last_difficulty = (
            difficulty
        )

        # Clear voice answer

        st.session_state.voice_answer = ""

        # Rerun

        st.rerun()


# =========================================================
# EVALUATION SECTION
# =========================================================

def render_evaluation_section(
    role,
    difficulty,
    company
):

    if "last_evaluation" not in st.session_state:

        return

    # -----------------------------------------------------
    # AI EVALUATION
    # -----------------------------------------------------

    st.divider()

    md(
        '<div class="section-title">'
        '📊 AI Evaluation'
        '</div>'
    )

    st.markdown(
        st.session_state.last_evaluation
    )

    # -----------------------------------------------------
    # FOLLOW-UP QUESTION
    # -----------------------------------------------------

    if st.session_state.get(
        "followup_question"
    ):

        st.divider()

        md(
            '<div class="section-title">'
            '🤖 AI Follow-up Question'
            '</div>'
        )

        st.info(
            st.session_state.followup_question
        )

        followup_answer = st.text_area(

            "✍️ Your Follow-up Answer",

            key="followup_answer",

            height=150,

            placeholder=
                "Answer the follow-up question..."
        )

        if st.button(
            "✅ Evaluate Follow-up",

            key="evaluate_followup",

            use_container_width=True
        ):

            if not followup_answer.strip():

                st.warning(
                    "Please answer the follow-up question."
                )

            else:

                with st.spinner(
                    "🤖 AI is evaluating your follow-up..."
                ):

                    followup_result = (
                        evaluate_answer(
                            st.session_state.followup_question,
                            followup_answer
                        )
                    )

                st.session_state.followup_evaluation = (
                    followup_result
                )

                st.rerun()

    # -----------------------------------------------------
    # FOLLOW-UP EVALUATION
    # -----------------------------------------------------

    if "followup_evaluation" not in st.session_state:

        return

    st.success(
        "✅ Follow-up Evaluated"
    )

    st.markdown(
        st.session_state.followup_evaluation
    )

    # -----------------------------------------------------
    # NEXT QUESTION
    # -----------------------------------------------------

    if (
        st.session_state.current_question
        <
        st.session_state.total_questions
    ):

        if st.button(
            "➡️ Next Question",

            key="next_question",

            use_container_width=True
        ):

            # Increment question

            st.session_state.current_question += 1

            # Generate new question

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

                st.session_state.question = (
                    question
                )

                # Clear evaluation data

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

                # Clear voice answer

                st.session_state.voice_answer = ""

                st.rerun()


# =========================================================
# COMPLETION SECTION
# =========================================================

def render_completion_section(
    role,
    difficulty,
    company
):

    if "followup_evaluation" not in st.session_state:

        return

    if (
        st.session_state.current_question
        !=
        st.session_state.total_questions
    ):

        return

    # -----------------------------------------------------
    # COMPLETED
    # -----------------------------------------------------

    st.divider()

    st.success(
        "🎉 Interview Completed!"
    )

    # -----------------------------------------------------
    # FINAL SCORE
    # -----------------------------------------------------

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

    st.session_state.average_score = (
        average
    )

    score_col1, score_col2, score_col3 = (
        st.columns(3)
    )

    with score_col1:

        st.metric(
            "⭐ Final Score",
            f"{average:.1f}/10"
        )

    with score_col2:

        st.metric(
            "📝 Questions",
            len(
                st.session_state.interview_questions
            )
        )

    with score_col3:

        st.metric(
            "🎯 Status",
            "Completed"
        )

    # -----------------------------------------------------
    # CAREER COACH
    # -----------------------------------------------------

    st.divider()

    if st.button(
        "🤖 Get AI Career Advice",

        key="career_advice_button",

        use_container_width=True
    ):

        with st.spinner(
            "🤖 AI Career Coach is analyzing your interview..."
        ):

            career_advice = (
                generate_career_advice(

                    role=role,

                    company=company,

                    difficulty=difficulty,

                    questions=
                        st.session_state.interview_questions,

                    answers=
                        st.session_state.interview_answers,

                    evaluations=
                        st.session_state.interview_evaluations,

                    scores=
                        st.session_state.scores
                )
            )

        st.session_state.career_advice = (
            career_advice
        )

    if "career_advice" in st.session_state:

        md(
            '<div class="section-title">'
            '🤖 AI Career Coach'
            '</div>'
        )

        st.markdown(
            st.session_state.career_advice
        )

    # -----------------------------------------------------
    # PDF REPORT
    # -----------------------------------------------------

    st.divider()

    if st.button(
        "📄 Generate PDF Report",

        key="generate_pdf",

        use_container_width=True
    ):

        filename = (
            "Interview_Report.pdf"
        )

        # Get last answer safely

        last_answer = (

            st.session_state
            .interview_answers[-1]

            if st.session_state.interview_answers

            else "Not Available"
        )

        generate_report(

            filename=filename,

            user=
                st.session_state.user["name"],

            role=
                st.session_state.get(
                    "last_role",
                    role
                ),

            difficulty=
                st.session_state.get(
                    "last_difficulty",
                    difficulty
                ),

            company=company,

            question=
                st.session_state.question,

            answer=
                last_answer,

            evaluation=
                st.session_state.get(
                    "last_evaluation",
                    "Not Available"
                ),

            overall_score=
                st.session_state.get(
                    "average_score",
                    0
                ),

            followup_question=
                st.session_state.get(
                    "followup_question",
                    "Not Available"
                ),

            followup_answer=
                st.session_state.get(
                    "followup_answer",
                    "Not Available"
                ),

            followup_evaluation=
                st.session_state.get(
                    "followup_evaluation",
                    "Not Available"
                ),

            career_advice=
                st.session_state.get(
                    "career_advice",
                    "Not Available"
                ),

            interview_questions=
                st.session_state.get(
                    "interview_questions",
                    []
                ),

            interview_answers=
                st.session_state.get(
                    "interview_answers",
                    []
                ),

            interview_evaluations=
                st.session_state.get(
                    "interview_evaluations",
                    []
                ),

            scores=
                st.session_state.get(
                    "scores",
                    []
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

                "⬇️ Download Interview Report",

                data=pdf,

                file_name=filename,

                mime="application/pdf",

                use_container_width=True
            )


# =========================================================
# FINISH INTERVIEW
# =========================================================

def finish_interview():

    # Change page first

    st.session_state.page = (
        "dashboard"
    )

    # Reset general interview state

    st.session_state.current_question = 1

    st.session_state.scores = []

    st.session_state.voice_answer = ""

    # Remove interview state

    keys_to_remove = [

        "question",

        "last_evaluation",

        "last_score",

        "last_role",

        "last_difficulty",

        "followup_question",

        "followup_evaluation",

        "career_advice",

        "average_score",

        "interview_questions",

        "interview_answers",

        "interview_evaluations",

        "followup_answer"
    ]

    for key in keys_to_remove:

        st.session_state.pop(
            key,
            None
        )

    # IMPORTANT:
    #
    # Do NOT manually pop candidate_answer_1,
    # candidate_answer_2, etc.
    #
    # Their keys are tied to widgets and Streamlit
    # will handle their lifecycle.
    #
    # The next page does not render these widgets anyway.

    st.rerun()


# =========================================================
# MAIN INTERVIEW PAGE
# =========================================================

def interview_page():

    # Initialize

    initialize_interview_state()

    # Load CSS

    load_interview_styles()

    # Setup

    (
        role,
        difficulty,
        company,
        question_count
    ) = render_interview_setup()

    # Question

    render_question_section(

        role=role,

        difficulty=difficulty,

        company=company
    )

    # Evaluation

    render_evaluation_section(

        role=role,

        difficulty=difficulty,

        company=company
    )

    # Completion

    render_completion_section(

        role=role,

        difficulty=difficulty,

        company=company
    )

    # -----------------------------------------------------
    # FINISH BUTTON
    # -----------------------------------------------------

    if (

        "followup_evaluation"
        in
        st.session_state

        and

        st.session_state.current_question
        ==
        st.session_state.total_questions

    ):

        st.divider()

        if st.button(

            "🏠 Finish Interview",

            key="finish_interview",

            use_container_width=True
        ):

            finish_interview()