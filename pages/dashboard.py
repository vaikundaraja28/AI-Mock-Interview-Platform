import streamlit as st
import pandas as pd
import plotly.express as px
from textwrap import dedent

from history.history_service import (
    get_statistics,
    get_scores,
    get_dashboard_data
)


# =========================================================
# HELPER
# =========================================================

def md(html: str):
    """
    Render HTML safely.
    Strips indentation from each line so Streamlit does not
    interpret HTML as a Markdown code block.
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
# DASHBOARD
# =========================================================

def dashboard():

    # =====================================================
    # PREMIUM DASHBOARD CSS
    # =====================================================

    md("""
    <style>

    /* =====================================================
       GLOBAL
    ===================================================== */

    #MainMenu,
    header,
    footer {
        visibility: hidden;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 10% 5%,
                rgba(79,124,255,0.10),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 10%,
                rgba(124,58,237,0.10),
                transparent 30%
            ),
            radial-gradient(
                circle at 50% 100%,
                rgba(56,189,248,0.05),
                transparent 40%
            ),
            #080D1C;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* =====================================================
       HEADER
    ===================================================== */

    .dashboard-header {
        padding: 20px 0 30px 0;
    }

    .dashboard-title {
        font-size: 40px;
        font-weight: 800;
        color: #F8FAFC;
        letter-spacing: -1.2px;
        margin-bottom: 8px;

        background:
            linear-gradient(
                135deg,
                #F8FAFC 35%,
                #A5B4FC 100%
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        display: inline-block;
    }

    .dashboard-subtitle {
        color: #8B96AC;
        font-size: 15px;
        line-height: 1.6;
    }


    /* =====================================================
       METRIC CARDS
    ===================================================== */

    .metric-card {
        position: relative;
        overflow: hidden;

        background:
            linear-gradient(
                155deg,
                rgba(19,26,45,0.96),
                rgba(13,18,32,0.96)
            );

        border: 1px solid #232D45;
        border-radius: 18px;

        padding: 24px;
        min-height: 145px;

        box-shadow:
            0 15px 40px rgba(0,0,0,0.25);

        transition:
            transform 0.22s ease,
            border-color 0.22s ease,
            box-shadow 0.22s ease;
    }

    .metric-card:hover {
        transform: translateY(-5px);

        border-color: #4F7CFF;

        box-shadow:
            0 18px 45px rgba(79,124,255,0.15);
    }

    .metric-icon {
        font-size: 25px;
        margin-bottom: 12px;
    }

    .metric-label {
        color: #8B96AC;
        font-size: 12px;
        font-weight: 700;

        text-transform: uppercase;
        letter-spacing: 0.7px;

        margin-bottom: 7px;
    }

    .metric-value {
        color: #F8FAFC;
        font-size: 32px;
        font-weight: 800;
        letter-spacing: -0.5px;
    }


    /* =====================================================
       SECTION TITLES
    ===================================================== */

    .section-title {
        font-size: 20px;
        font-weight: 750;

        color: #F8FAFC;

        margin-top: 32px;
        margin-bottom: 16px;
    }


    /* =====================================================
       ACTION CARDS
    ===================================================== */

    .action-card {
        background:
            linear-gradient(
                155deg,
                #131A2D,
                #0E1424
            );

        border: 1px solid #232D45;
        border-radius: 16px;

        padding: 22px;
        min-height: 130px;

        transition:
            transform 0.25s ease,
            border-color 0.25s ease,
            box-shadow 0.25s ease;
    }

    .action-card:hover {
        transform: translateY(-4px);

        border-color: #4F7CFF;

        box-shadow:
            0 12px 32px rgba(79,124,255,0.15);
    }

    .action-icon {
        font-size: 25px;
        margin-bottom: 10px;
    }

    .action-title {
        color: #F8FAFC;
        font-size: 15px;
        font-weight: 700;
    }

    .action-description {
        color: #8B96AC;
        font-size: 12.5px;

        margin-top: 6px;

        line-height: 1.5;
    }


    /* =====================================================
       BUTTONS
    ===================================================== */

    .stButton > button {

        background:
            linear-gradient(
                135deg,
                #4F7CFF,
                #635BFF
            );

        color: white;

        border: none;
        border-radius: 10px;

        height: 44px;

        font-weight: 650;

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }

    .stButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
            0 10px 25px
            rgba(79,124,255,0.28);
    }


    /* =====================================================
       EMPTY STATE
    ===================================================== */

    .empty-state {

        background:
            rgba(17,24,39,0.7);

        border:
            1px dashed #334155;

        border-radius: 16px;

        padding: 40px;

        text-align: center;

        color: #8B96AC;

        margin-top: 10px;
    }


    /* =====================================================
       RESPONSIVE
    ===================================================== */

    @media (max-width: 768px) {

        .dashboard-title {
            font-size: 28px;
        }

        .dashboard-subtitle {
            font-size: 14px;
        }

        .metric-card {
            margin-bottom: 10px;
        }

    }

    </style>
    """)


    # =====================================================
    # HEADER
    # =====================================================

    user_name = st.session_state.user["name"]

    md(f"""
    <div class="dashboard-header">

        <div class="dashboard-title">
            Welcome back, {user_name} 👋
        </div>

        <div class="dashboard-subtitle">
            Track your interview performance,
            improve your skills, and prepare for your next opportunity.
        </div>

    </div>
    """)


    # =====================================================
    # FETCH DATA
    # =====================================================

    user_id = st.session_state.user["id"]

    stats = get_statistics(user_id)

    interviews = stats[0] or 0

    average = (
        round(stats[1], 1)
        if stats[1]
        else 0
    )

    highest = (
        stats[2]
        if stats[2]
        else 0
    )

    scores = get_scores(user_id)

    dashboard_data = get_dashboard_data(user_id)


    # =====================================================
    # PERFORMANCE OVERVIEW
    # =====================================================

    md("""
    <div class="section-title">
        📊 Performance Overview
    </div>
    """)

    c1, c2, c3 = st.columns(
        3,
        gap="large"
    )


    # INTERVIEWS

    with c1:

        md(f"""
        <div class="metric-card">

            <div class="metric-icon">
                🎤
            </div>

            <div class="metric-label">
                Interviews Completed
            </div>

            <div class="metric-value">
                {interviews}
            </div>

        </div>
        """)


    # AVERAGE SCORE

    with c2:

        md(f"""
        <div class="metric-card">

            <div class="metric-icon">
                ⭐
            </div>

            <div class="metric-label">
                Average Score
            </div>

            <div class="metric-value">
                {average}/10
            </div>

        </div>
        """)


    # HIGHEST SCORE

    with c3:

        md(f"""
        <div class="metric-card">

            <div class="metric-icon">
                🏆
            </div>

            <div class="metric-label">
                Highest Score
            </div>

            <div class="metric-value">
                {highest}/10
            </div>

        </div>
        """)


    # =====================================================
    # QUICK ACTIONS
    # =====================================================

    md("""
    <div class="section-title">
        ⚡ Quick Actions
    </div>
    """)

    col1, col2, col3 = st.columns(
        3,
        gap="large"
    )


    # START INTERVIEW

    with col1:

        md("""
        <div class="action-card">

            <div class="action-icon">
                🚀
            </div>

            <div class="action-title">
                Start Mock Interview
            </div>

            <div class="action-description">
                Practice real-world interviews
                with AI-powered questions and feedback.
            </div>

        </div>
        """)

        if st.button(
            "Start Interview",
            key="start_interview",
            use_container_width=True
        ):

            st.session_state.page = "interview"

            st.rerun()


    # RESUME ANALYZER

    with col2:

        md("""
        <div class="action-card">

            <div class="action-icon">
                📄
            </div>

            <div class="action-title">
                Resume Analyzer
            </div>

            <div class="action-description">
                Upload your resume and receive
                AI-powered feedback and suggestions.
            </div>

        </div>
        """)

        if st.button(
            "Analyze Resume",
            key="upload_resume",
            use_container_width=True
        ):

            st.session_state.page = "resume"

            st.rerun()


    # INTERVIEW HISTORY

    with col3:

        md("""
        <div class="action-card">

            <div class="action-icon">
                📜
            </div>

            <div class="action-title">
                Interview History
            </div>

            <div class="action-description">
                Review your previous interviews,
                scores, and AI evaluations.
            </div>

        </div>
        """)

        if st.button(
            "View History",
            key="history",
            use_container_width=True
        ):

            st.session_state.page = "history"

            st.rerun()


    # =====================================================
    # PERFORMANCE CHART
    # =====================================================

    md("""
    <div class="section-title">
        📈 Interview Performance
    </div>
    """)


    if len(scores) > 0:

        data = pd.DataFrame(
            scores,
            columns=[
                "Role",
                "Difficulty",
                "Score",
                "Question",
                "Company",
                "Date"
            ]
        )

        data["Interview"] = range(
            1,
            len(data) + 1
        )


        fig = px.line(
            data,
            x="Interview",
            y="Score",
            markers=True,
            hover_data=[
                "Role",
                "Difficulty",
                "Company",
                "Question",
                "Date"
            ]
        )


        fig.update_traces(
            line_color="#4F7CFF",
            marker=dict(
                size=8,
                color="#7C6FFF"
            )
        )


        fig.update_layout(

            title={
                "text": "Score Progress",
                "font": {
                    "color": "#F8FAFC"
                }
            },

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            font={
                "color": "#CBD5E1"
            },

            xaxis={
                "title": "Interview Number",
                "gridcolor": "#232D45"
            },

            yaxis={
                "title": "Score",
                "range": [0, 10],
                "gridcolor": "#232D45"
            },

            margin={
                "l": 30,
                "r": 30,
                "t": 50,
                "b": 30
            }
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    else:

        md("""
        <div class="empty-state">

            <div style="font-size:35px;">
                📈
            </div>

            <div style="
                color:#F8FAFC;
                font-size:17px;
                font-weight:600;
                margin-top:10px;
            ">
                No performance data yet
            </div>

            <div style="margin-top:8px;">
                Complete your first mock interview
                to start tracking your progress.
            </div>

        </div>
        """)


    # =====================================================
    # ANALYTICS
    # =====================================================

    md("""
    <div class="section-title">
        📊 Analytics
    </div>
    """)


    if len(dashboard_data) > 0:

        df = pd.DataFrame(
            dashboard_data,
            columns=[
                "Role",
                "Difficulty",
                "Company",
                "Score",
                "Date"
            ]
        )


        left, right = st.columns(
            2,
            gap="large"
        )


        # =================================================
        # ROLE DISTRIBUTION
        # =================================================

        with left:

            role_counts = (
                df["Role"]
                .value_counts()
                .reset_index()
            )

            role_counts.columns = [
                "Role",
                "Count"
            ]


            role_chart = px.bar(
                role_counts,
                x="Role",
                y="Count",
                text="Count"
            )


            role_chart.update_traces(
                marker_color="#4F7CFF"
            )


            role_chart.update_layout(

                title={
                    "text": "Interviews by Role",
                    "font": {
                        "color": "#F8FAFC"
                    }
                },

                paper_bgcolor="rgba(0,0,0,0)",

                plot_bgcolor="rgba(0,0,0,0)",

                font={
                    "color": "#CBD5E1"
                },

                xaxis={
                    "gridcolor": "#232D45"
                },

                yaxis={
                    "gridcolor": "#232D45"
                }
            )


            st.plotly_chart(
                role_chart,
                use_container_width=True
            )


        # =================================================
        # DIFFICULTY DISTRIBUTION
        # =================================================

        with right:

            difficulty_chart = px.pie(
                df,
                names="Difficulty",
                hole=0.55,
                color_discrete_sequence=[
                    "#4F7CFF",
                    "#635BFF",
                    "#38BDF8"
                ]
            )


            difficulty_chart.update_layout(

                title={
                    "text": "Difficulty Distribution",
                    "font": {
                        "color": "#F8FAFC"
                    }
                },

                paper_bgcolor="rgba(0,0,0,0)",

                font={
                    "color": "#CBD5E1"
                }
            )


            st.plotly_chart(
                difficulty_chart,
                use_container_width=True
            )


    else:

        md("""
        <div class="empty-state">

            📊

            <div style="
                margin-top:10px;
                color:#F8FAFC;
                font-size:16px;
                font-weight:600;
            ">
                No interview analytics available yet.
            </div>

            <div style="margin-top:8px;">
                Complete an interview to unlock
                detailed performance analytics.
            </div>

        </div>
        """)