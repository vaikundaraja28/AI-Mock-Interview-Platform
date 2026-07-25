import streamlit as st

from history.history_service import (
    get_history,
    get_interview
)


# =========================================================
# SAFE HTML RENDERER
# =========================================================

def md(html: str):

    lines = [
        line.strip()
        for line in html.strip("\n").splitlines()
    ]

    st.markdown(
        "\n".join(lines),
        unsafe_allow_html=True
    )


# =========================================================
# HISTORY PAGE STYLES
# =========================================================

def load_history_styles():

    md("""
        <style>

        #MainMenu,
        header,
        footer {
            visibility: hidden;
        }

        .stApp {

            background:
                radial-gradient(
                    circle at 8% 8%,
                    rgba(79,124,255,0.10),
                    transparent 32%
                ),

                radial-gradient(
                    circle at 92% 12%,
                    rgba(124,58,237,0.10),
                    transparent 32%
                ),

                #080D1C;
        }

        .block-container {

            max-width: 1000px;

            padding-top: 2rem;

            padding-bottom: 3rem;
        }


        /* =================================================
           HEADER
        ================================================= */

        .history-header {

            margin-bottom: 1.75rem;
        }

        .history-title {

            font-size: 2.2rem;

            font-weight: 800;

            color: #F8FAFC;

            letter-spacing: -0.8px;

            margin-bottom: 0.4rem;
        }

        .history-subtitle {

            font-size: 0.98rem;

            color: #8B96AC;

            line-height: 1.5;
        }


        /* =================================================
           SUMMARY CARDS
        ================================================= */

        .summary-card {

            background:
                linear-gradient(
                    155deg,
                    rgba(19,26,45,0.95),
                    rgba(13,18,32,0.95)
                );

            border: 1px solid #232D45;

            border-radius: 16px;

            padding: 18px 22px;

            text-align: center;
        }

        .summary-value {

            color: #F8FAFC;

            font-size: 24px;

            font-weight: 800;
        }

        .summary-label {

            color: #8B96AC;

            font-size: 11.5px;

            font-weight: 600;

            text-transform: uppercase;

            letter-spacing: 0.6px;

            margin-top: 4px;
        }


        /* =================================================
           EMPTY STATE
        ================================================= */

        .empty-state {

            background: #111827;

            border: 1px dashed #334155;

            border-radius: 16px;

            padding: 40px;

            text-align: center;

            color: #8B96AC;

            margin-top: 20px;
        }


        /* =================================================
           LABELS
        ================================================= */

        .block-label {

            color: #8EA8FF;

            font-size: 0.8rem;

            font-weight: 700;

            text-transform: uppercase;

            letter-spacing: 0.6px;

            margin-top: 18px;

            margin-bottom: 8px;
        }


        /* =================================================
           TAGS
        ================================================= */

        .tag-chip {

            background: rgba(79,124,255,0.10);

            border: 1px solid rgba(79,124,255,0.25);

            color: #A5B4FC;

            border-radius: 999px;

            padding: 5px 12px;

            margin-right: 6px;

            display: inline-block;

            font-size: 0.82rem;

            font-weight: 600;
        }


        /* =================================================
           EXPANDER
        ================================================= */

        [data-testid="stExpander"] {

            background:
                linear-gradient(
                    145deg,
                    #111827,
                    #0F172A
                );

            border: 1px solid #25304A !important;

            border-radius: 16px !important;

            margin-bottom: 14px;

            box-shadow:
                0 12px 30px rgba(0,0,0,0.18);

            overflow: hidden;
        }


        [data-testid="stExpander"] summary {

            padding: 14px 18px !important;
        }


        [data-testid="stExpander"] summary:hover {

            background:
                rgba(79,124,255,0.06);
        }


        /* =================================================
           BUTTON
        ================================================= */

        .stButton > button {

            border-radius: 10px;

            font-weight: 650;

            height: 44px;

            background:
                linear-gradient(
                    135deg,
                    #4F7CFF,
                    #635BFF
                );

            color: white;

            border: none;
        }

        .stButton > button:hover {

            transform: translateY(-2px);

            box-shadow:
                0 10px 25px
                rgba(79,124,255,0.28);
        }

        </style>
    """)


# =========================================================
# SCORE COLOR
# =========================================================

def score_color(score):

    if score >= 8:

        return "#4ADE80"

    elif score >= 5:

        return "#FACC15"

    else:

        return "#F87171"


# =========================================================
# HISTORY PAGE
# =========================================================

def history_page():

    load_history_styles()


    # =====================================================
    # BACK TO DASHBOARD
    # =====================================================

    if st.button(
        "← Back to Dashboard",
        key="back_to_dashboard"
    ):

        st.session_state.page = "dashboard"

        st.rerun()


    # =====================================================
    # HEADER
    # =====================================================

    md("""
        <div class="history-header">

            <div class="history-title">
                📜 Interview History
            </div>

            <div class="history-subtitle">
                Review your past mock interviews,
                answers, and AI feedback.
            </div>

        </div>
    """)


    # =====================================================
    # GET USER ID
    # =====================================================

    user_id = st.session_state.user["id"]


    # =====================================================
    # GET HISTORY FROM DATABASE
    # =====================================================

    history = get_history(user_id)


    # =====================================================
    # EMPTY STATE
    # =====================================================

    if not history:

        md("""
            <div class="empty-state">

                <div style="font-size:35px;">
                    📭
                </div>

                <div
                    style="
                    color:#F8FAFC;
                    font-size:17px;
                    font-weight:600;
                    margin-top:10px;
                    "
                >
                    No interviews yet
                </div>

                <div style="margin-top:8px;">

                    Complete a mock interview
                    to see your history here.

                </div>

            </div>
        """)

        return


    # =====================================================
    # CALCULATE SUMMARY
    # =====================================================

    total = len(history)

    scores = []


    for interview in history:

        try:

            # IMPORTANT:
            #
            # get_history() returns:
            #
            # 0 = id
            # 1 = role
            # 2 = difficulty
            # 3 = company
            # 4 = score
            # 5 = created_at
            #
            score = interview[4]

            if score is not None:

                scores.append(float(score))

        except (
            TypeError,
            ValueError,
            IndexError
        ):

            continue


    if scores:

        average_score = round(
            sum(scores) / len(scores),
            1
        )

        best_score = max(scores)

    else:

        average_score = 0

        best_score = 0


    # =====================================================
    # SUMMARY CARDS
    # =====================================================

    col1, col2, col3 = st.columns(3)


    with col1:

        md(f"""
            <div class="summary-card">

                <div class="summary-value">
                    {total}
                </div>

                <div class="summary-label">
                    Total Interviews
                </div>

            </div>
        """)


    with col2:

        md(f"""
            <div class="summary-card">

                <div class="summary-value">
                    {average_score}/10
                </div>

                <div class="summary-label">
                    Average Score
                </div>

            </div>
        """)


    with col3:

        md(f"""
            <div class="summary-card">

                <div class="summary-value">
                    {best_score}/10
                </div>

                <div class="summary-label">
                    Best Score
                </div>

            </div>
        """)


    md(
        "<div style='height:22px'></div>"
    )


    # =====================================================
    # INTERVIEW HISTORY
    # =====================================================

    for interview in history:


        # =================================================
        # CORRECT DATABASE COLUMN MAPPING
        # =================================================

        interview_id = interview[0]

        role = interview[1]

        difficulty = interview[2]

        company = interview[3]

        score = interview[4]

        date = interview[5]


        # =================================================
        # CONVERT SCORE
        # =================================================

        try:

            score = (
                float(score)
                if score is not None
                else 0
            )

        except (
            TypeError,
            ValueError
        ):

            score = 0


        color = score_color(score)


        # =================================================
        # INTERVIEW EXPANDER
        # =================================================

        with st.expander(
            f"⭐ {score:.1f}/10  ·  "
            f"{role}  ·  "
            f"{difficulty}"
        ):


            # =============================================
            # META TAGS
            # =============================================

            md(
                f"""
                <div>

                    <span class="tag-chip">
                        🆔 ID {interview_id}
                    </span>

                    <span class="tag-chip">
                        💼 {role}
                    </span>

                    <span class="tag-chip">
                        🏢 {company}
                    </span>

                    <span class="tag-chip">
                        🎯 {difficulty}
                    </span>

                    <span
                        class="tag-chip"
                        style="
                            color:{color};
                            border-color:{color}44;
                            background:{color}1A;
                        "
                    >
                        ⭐ {score:.1f}/10
                    </span>

                    <span class="tag-chip">
                        📅 {date}
                    </span>

                </div>
                """
            )


            st.divider()


            # =============================================
            # GET FULL INTERVIEW
            # =============================================

            interview_data = get_interview(
                interview_id
            )


            if interview_data:

                question = interview_data[0]

                answer = interview_data[1]

                evaluation = interview_data[2]


                # =========================================
                # QUESTION
                # =========================================

                md(
                    '<div class="block-label">'
                    '📄 Interview Question'
                    '</div>'
                )

                st.info(question)


                # =========================================
                # ANSWER
                # =========================================

                md(
                    '<div class="block-label">'
                    '💬 Your Answer'
                    '</div>'
                )

                st.write(answer)


                # =========================================
                # AI EVALUATION
                # =========================================

                md(
                    '<div class="block-label">'
                    '🤖 AI Evaluation'
                    '</div>'
                )

                st.markdown(
                    evaluation
                )

            else:

                st.warning(
                    "Interview details could not be found."
                )