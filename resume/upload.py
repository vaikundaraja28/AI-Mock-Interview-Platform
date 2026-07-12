import streamlit as st

from utils.pdf_parser import extract_pdf_text
from resume.analysis import analyze_resume


def upload_resume():

    st.title("📄 Resume Upload")

    st.write("Upload your resume to receive an AI-powered analysis.")

    uploaded = st.file_uploader(
        "Choose your resume",
        type=["pdf", "docx"]
    )

    if uploaded is not None:

        st.success("✅ Resume uploaded successfully!")

        st.write(f"**Filename:** {uploaded.name}")
        st.write(f"**Size:** {round(uploaded.size / 1024, 2)} KB")

        if uploaded.name.endswith(".pdf"):

            if st.button(
                "🤖 Analyze Resume",
                use_container_width=True
            ):

                text = extract_pdf_text(uploaded)

                st.session_state.resume_text = text

                analyze_resume(text)

        else:

            st.warning(
                "DOCX support will be added in the next update. Please upload a PDF for now."
            )

    if st.button(
        "⬅ Back to Dashboard",
        use_container_width=True
    ):

        st.session_state.page = "dashboard"
        st.rerun()