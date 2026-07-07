import streamlit as st


def upload_resume():

    st.title("📄 Resume Upload")

    uploaded = st.file_uploader(
        "Upload your resume",
        type=[
            "pdf",
            "docx"
        ]
    )

    if uploaded:

        st.success("Resume uploaded successfully!")

        st.write("Filename:", uploaded.name)

        st.write("Size:", uploaded.size, "bytes")

        if st.button("Continue to AI Analysis"):

            st.session_state.page = "analysis"

            st.rerun()