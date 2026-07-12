import streamlit as st
import pandas as pd
import plotly.express as px

from history.history_service import (
    get_statistics,
    get_scores,
    get_dashboard_data
)


def dashboard():

    st.title("🏠 Dashboard")

    st.write(f"Welcome back, **{st.session_state.user['name']}** 👋")

    st.write("")

    # ==========================
    # Statistics
    # ==========================

    stats = get_statistics(st.session_state.user["id"])

    interviews = stats[0] or 0
    average = round(stats[1], 1) if stats[1] else 0
    highest = stats[2] or 0

    scores = get_scores(st.session_state.user["id"])

    dashboard_data = get_dashboard_data(
        st.session_state.user["id"]
    )

    # ==========================
    # Metrics
    # ==========================

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🎤 Interviews",
            interviews
        )

    with c2:
        st.metric(
            "⭐ Average Score",
            f"{average}/10"
        )

    with c3:
        st.metric(
            "🏆 Highest Score",
            f"{highest}/10"
        )

    st.divider()

    # ==========================
    # Quick Actions
    # ==========================

    st.subheader("Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "🚀 Start Interview",
            key="start_interview",
            use_container_width=True
        ):
            st.session_state.page = "interview"
            st.rerun()

    with col2:

        if st.button(
            "📄 Upload Resume",
            key="upload_resume",
            use_container_width=True
        ):
            st.session_state.page = "resume"
            st.rerun()

    with col3:

        if st.button(
            "📜 Interview History",
            key="history",
            use_container_width=True
        ):
            st.session_state.page = "history"
            st.rerun()

    # ==========================
    # Performance Chart
    # ==========================

    st.divider()

    st.subheader("📈 Interview Performance")

    if len(scores) > 0:

        data = pd.DataFrame(
            scores,
            columns=[
                "Role",
                "Difficulty",
                "Score",
                "Question",
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
                "Question",
                "Date"
            ],
            title="Score Progress"
        )

        fig.update_layout(
            xaxis_title="Interview Number",
            yaxis_title="Score",
            yaxis=dict(range=[0, 10])
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info(
            "Complete your first interview to see your progress."
        )

    # ==========================
    # Analytics
    # ==========================

    st.divider()

    st.subheader("📊 Analytics")

    if len(dashboard_data) > 0:

        df = pd.DataFrame(
            dashboard_data,
            columns=[
                "Role",
                "Difficulty",
                "Score",
                "Date"
            ]
        )

        left, right = st.columns(2)

        # ----------------------
        # Role Bar Chart
        # ----------------------

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
                title="Interviews by Role",
                text="Count"
            )

            st.plotly_chart(
                role_chart,
                use_container_width=True
            )

        # ----------------------
        # Difficulty Pie Chart
        # ----------------------

        with right:

            difficulty_chart = px.pie(
                df,
                names="Difficulty",
                title="Difficulty Distribution"
            )

            st.plotly_chart(
                difficulty_chart,
                use_container_width=True
            )

    else:

        st.info("No interview data available yet.")