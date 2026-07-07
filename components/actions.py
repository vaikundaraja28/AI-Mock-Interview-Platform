import streamlit as st


def actions():

    left, right = st.columns(2, gap="large")

    with left:

        st.markdown("## 🧠 Start Interview")

        st.write(
            "Practice HR, Technical and Aptitude interviews using AI."
        )

        if st.button(
            "🚀 Launch Interview",
            key="start_interview",
            use_container_width=True
        ):
            st.success("Interview page will be added soon.")

    with right:

        st.markdown("## 📄 Upload Resume")

        st.write(
            "Analyze your resume and receive AI-powered suggestions."
        )

        if st.button(
            "📤 Analyze Resume",
            key="resume_upload",
            use_container_width=True
        ):
            st.success("Resume Analyzer will be added soon.")