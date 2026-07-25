import streamlit as st

from utils.pdf_parser import extract_pdf_text
from resume.analysis import analyze_resume


def md(html: str):
    """Render HTML safely."""
    lines = [
        line.strip()
        for line in html.strip("\n").splitlines()
    ]

    st.markdown(
        "\n".join(lines),
        unsafe_allow_html=True
    )


def load_resume_styles():

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
            max-width: 900px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }


        /* ================================
           HEADER
        ================================= */

        .resume-header {
            margin-bottom: 1.75rem;
        }

        .resume-title {
            font-size: 2.2rem;
            font-weight: 800;
            color: #F8FAFC;
            letter-spacing: -0.8px;
            margin-bottom: 0.4rem;

            background:
                linear-gradient(
                    135deg,
                    #F8FAFC 40%,
                    #A5B4FC 100%
                );

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;

            display: inline-block;
        }

        .resume-subtitle {
            font-size: 0.98rem;
            color: #8B96AC;
            line-height: 1.5;
        }


        /* ================================
           UPLOAD CARD
        ================================= */

        .upload-card {
            background:
                linear-gradient(
                    155deg,
                    rgba(19,26,45,0.95),
                    rgba(13,18,32,0.95)
                );

            border: 1px dashed #334155;
            border-radius: 18px;

            padding: 32px;

            margin-bottom: 1.25rem;
        }

        .upload-card:hover {
            border-color: #4F7CFF;
        }

        .upload-icon {
            font-size: 30px;
            margin-bottom: 8px;
        }

        .upload-label {
            color: #F8FAFC;
            font-size: 1rem;
            font-weight: 700;
            margin-bottom: 4px;
        }

        .upload-hint {
            color: #8B96AC;
            font-size: 0.85rem;
        }


        /* ================================
           FILE UPLOADER
        ================================= */

        [data-testid="stFileUploader"] {
            background: transparent;
        }

        [data-testid="stFileUploaderDropzone"] {
            background: #0B1222 !important;
            border: 1px solid #25304A !important;
            border-radius: 12px !important;
        }


        /* ================================
           FILE CARD
        ================================= */

        .file-card {
            background:
                linear-gradient(
                    145deg,
                    #111827,
                    #0F172A
                );

            border: 1px solid #25304A;
            border-radius: 16px;

            padding: 20px 24px;

            margin-top: 1rem;
            margin-bottom: 1.25rem;

            box-shadow:
                0 12px 30px
                rgba(0,0,0,0.18);

            display: flex;
            align-items: center;
            gap: 16px;
        }

        .file-icon {
            font-size: 26px;

            background:
                rgba(79,124,255,0.12);

            border-radius: 12px;

            padding: 12px 14px;
        }

        .file-name {
            color: #F8FAFC;
            font-size: 1rem;
            font-weight: 700;
        }

        .file-meta {
            color: #8EA8FF;
            font-size: 0.82rem;
            font-weight: 600;
            margin-top: 2px;
        }


        /* ================================
           ATS SCORE CARD
        ================================= */

        .ats-score-card {

            position: relative;

            background:
                linear-gradient(
                    145deg,
                    rgba(25,35,65,0.98),
                    rgba(13,18,32,0.98)
                );

            border:
                1px solid
                rgba(79,124,255,0.45);

            border-radius: 22px;

            padding: 32px 28px;

            margin: 25px 0 30px 0;

            text-align: center;

            box-shadow:
                0 20px 50px
                rgba(0,0,0,0.30),

                0 0 40px
                rgba(79,124,255,0.08);
        }


        .ats-label {

            color: #A5B4FC;

            font-size: 0.95rem;

            font-weight: 800;

            text-transform: uppercase;

            letter-spacing: 1.5px;

            margin-bottom: 8px;
        }


        .ats-score {

            font-size: 5rem;

            line-height: 1;

            font-weight: 900;

            letter-spacing: -3px;

            color: #F8FAFC;

            text-shadow:
                0 0 25px
                rgba(79,124,255,0.35);
        }


        .ats-out-of {

            font-size: 1.3rem;

            font-weight: 700;

            color: #8B96AC;

            margin-left: 6px;
        }


        .ats-status {

            margin-top: 14px;

            font-size: 0.95rem;

            font-weight: 700;

            color: #CBD5E1;
        }


        /* ================================
           ANALYSIS CARD
        ================================= */

        .analysis-card {

            background:
                linear-gradient(
                    145deg,
                    rgba(17,24,39,0.90),
                    rgba(15,23,42,0.90)
                );

            border:
                1px solid #25304A;

            border-radius: 18px;

            padding: 26px;

            margin-top: 20px;
        }


        /* ================================
           BUTTONS
        ================================= */

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

            transform:
                translateY(-1px);

            box-shadow:
                0 8px 20px
                rgba(79,124,255,0.25);
        }


        /* ================================
           MOBILE
        ================================= */

        @media (max-width: 768px) {

            .resume-title {
                font-size: 1.8rem;
            }

            .upload-card {
                padding: 22px;
            }

            .file-card {

                flex-direction: column;

                align-items: flex-start;
            }

            .ats-score {

                font-size: 4rem;
            }
        }

        </style>
    """)


def get_ats_status(score):

    if score is None:
        return "Unable to determine ATS score."

    if score >= 80:
        return "🟢 Excellent ATS compatibility"

    elif score >= 60:
        return "🟡 Good ATS compatibility — some improvements recommended"

    elif score >= 40:
        return "🟠 Moderate ATS compatibility — improvements needed"

    else:
        return "🔴 Low ATS compatibility — significant improvements recommended"


def render_ats_score(ats_score):
    """
    Render the ATS score card exactly once.
    """

    if ats_score is None:
        st.warning(
            "⚠️ ATS score could not be extracted from the AI analysis."
        )
        return

    status = get_ats_status(ats_score)

    md(f"""
        <div class="ats-score-card">

            <div class="ats-label">
                🎯 ATS Compatibility Score
            </div>

            <div class="ats-score">
                {ats_score}
                <span class="ats-out-of">
                    / 100
                </span>
            </div>

            <div class="ats-status">
                {status}
            </div>

        </div>
    """)


def upload_resume():

    load_resume_styles()

    # ==========================================
    # HEADER
    # ==========================================

    md("""
        <div class="resume-header">

            <div class="resume-title">
                📄 Resume Analyzer
            </div>

            <div class="resume-subtitle">
                Upload your resume to receive an AI-powered analysis of your
                skills, experience, ATS compatibility, and fit for your target role.
            </div>

        </div>
    """)


    # ==========================================
    # UPLOAD ZONE
    # ==========================================

    md("""
        <div class="upload-card">

            <div class="upload-icon">
                📤
            </div>

            <div class="upload-label">
                Drop your resume here
            </div>

            <div class="upload-hint">
                Supports PDF and DOCX · Max 200MB
            </div>

        </div>
    """)


    uploaded = st.file_uploader(
        "Choose your resume",
        type=["pdf", "docx"],
        label_visibility="collapsed"
    )


    # ==========================================
    # FILE INFORMATION
    # ==========================================

    if uploaded is not None:

        st.success(
            "✅ Resume uploaded successfully!"
        )

        size_kb = round(
            uploaded.size / 1024,
            2
        )

        md(f"""
            <div class="file-card">

                <div class="file-icon">
                    📎
                </div>

                <div>

                    <div class="file-name">
                        {uploaded.name}
                    </div>

                    <div class="file-meta">
                        {size_kb} KB
                    </div>

                </div>

            </div>
        """)


        # ======================================
        # PDF
        # ======================================

        if uploaded.name.lower().endswith(".pdf"):

            if st.button(
                "🤖 Analyze Resume",
                key="analyze_resume",
                use_container_width=True
            ):

                with st.spinner(
                    "🤖 Extracting and analyzing your resume..."
                ):

                    text = extract_pdf_text(
                        uploaded
                    )

                    st.session_state.resume_text = text

                    # Clear old analysis
                    st.session_state.pop(
                        "resume_analysis",
                        None
                    )

                    st.session_state.pop(
                        "ats_score",
                        None
                    )

                    # Analyze resume
                    result = analyze_resume(
                        text
                    )

                if result and result.startswith("ERROR"):

                    st.error(result)

                else:

                    st.success(
                        "✅ Resume analysis completed!"
                    )

                    # IMPORTANT:
                    # Do NOT render ATS score here.
                    #
                    # The ATS score will be rendered only once
                    # in the section below using session_state.

                    st.rerun()


        # ======================================
        # DOCX
        # ======================================

        else:

            st.warning(
                "DOCX support will be added in the next update. "
                "Please upload a PDF for now."
            )


    # ==========================================
    # DISPLAY SAVED ANALYSIS
    # ATS SCORE IS RENDERED ONLY HERE
    # ==========================================

    if "resume_analysis" in st.session_state:

        ats_score = st.session_state.get(
            "ats_score"
        )

        # --------------------------------------
        # ATS SCORE — ONLY ONE DISPLAY
        # --------------------------------------

        render_ats_score(
            ats_score
        )


        # --------------------------------------
        # AI ANALYSIS
        # --------------------------------------

        md("""
            <div class="analysis-card">

                <h3 style="color:#F8FAFC;">
                    🤖 AI Resume Analysis
                </h3>

            </div>
        """)

        st.markdown(
            st.session_state.resume_analysis
        )


    # ==========================================
    # BACK TO DASHBOARD
    # ==========================================

    st.divider()

    if st.button(
        "⬅ Back to Dashboard",
        key="back_to_dashboard",
        use_container_width=True
    ):

        st.session_state.pop(
            "resume_analysis",
            None
        )

        st.session_state.pop(
            "ats_score",
            None
        )

        st.session_state.pop(
            "resume_text",
            None
        )

        st.session_state.page = "dashboard"

        st.rerun()