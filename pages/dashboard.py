import streamlit as st
from history.history_service import get_statistics

def dashboard():

    st.title("🏠 Dashboard")

    st.write(f"Welcome back, **{st.session_state.user['name']}** 👋")

    st.write("")
    stats = get_statistics(
    st.session_state.user["id"]
)

    interviews = stats[0] or 0
    average = stats[1] or 0
    highest = stats[2] or 0

    c1, c2, c3 = st.columns(3)

    with c1:
     st.metric(
        "Interviews",
        interviews
    )

    with c2:
     st.metric(
        "Average Score",
        f"{average:.1f}/10"
    )

    with c3:
     st.metric(
        "Highest Score",
        f"{highest}/10"
    )

    st.divider()

    st.subheader("Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "🚀 Start Interview",
            use_container_width=True,
            key="start_interview"
        ):
            st.session_state.page = "interview"
            st.rerun()

    with col2:

        if st.button(
            "📄 Upload Resume",
            use_container_width=True,
            key="upload_resume"
        ):
            st.session_state.page = "resume"
            st.rerun()
    with col3:

        if st.button(
        "📜 Interview History",
        use_container_width=True
        ):
            st.session_state.page = "history"
            st.rerun()