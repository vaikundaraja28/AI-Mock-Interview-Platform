import streamlit as st

from services.auth_service import login
from auth.session import login_user


def render_html(html: str) -> None:
    """
    Render raw HTML/CSS safely using Streamlit.
    """

    lines = [
        line.strip()
        for line in html.strip().splitlines()
        if line.strip()
    ]

    st.markdown(
        "\n".join(lines),
        unsafe_allow_html=True
    )


def login_page():

    # =========================================================
    # PREMIUM LOGIN PAGE - CUSTOM CSS
    # =========================================================

    st.markdown(
        """
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');


        /* =====================================================
           GLOBAL
        ===================================================== */

        * {
            font-family: 'Inter', -apple-system, sans-serif;
        }

        #MainMenu,
        footer,
        header {
            visibility: hidden;
        }

        .stApp {
            background:
                radial-gradient(
                    circle at 8% 15%,
                    rgba(99, 102, 241, 0.16),
                    transparent 40%
                ),
                radial-gradient(
                    circle at 92% 25%,
                    rgba(168, 85, 247, 0.14),
                    transparent 40%
                ),
                radial-gradient(
                    circle at 50% 90%,
                    rgba(56, 189, 248, 0.08),
                    transparent 45%
                ),
                #05070F;

            background-attachment: fixed;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }


        /* =====================================================
           ANIMATIONS
        ===================================================== */

        @keyframes fadeSlideUp {

            from {
                opacity: 0;
                transform: translateY(18px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }

        }


        /* =====================================================
           MAIN WRAPPER
        ===================================================== */

        .login-wrapper {
            max-width: 1160px;
            margin: 50px auto 30px auto;
            padding: 10px;
        }


        /* =====================================================
           LEFT BRANDING
        ===================================================== */

        .brand-section {
            padding: 55px 40px 40px 20px;
            color: #F8FAFC;
            animation: fadeSlideUp 0.7s ease both;
        }


        /* =====================================================
           BRAND BADGE
        ===================================================== */

        .brand-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;

            padding: 9px 16px;
            margin-bottom: 28px;

            background:
                linear-gradient(
                    135deg,
                    rgba(99, 102, 241, 0.18),
                    rgba(168, 85, 247, 0.14)
                );

            border:
                1px solid
                rgba(129, 140, 248, 0.35);

            border-radius: 999px;

            color: #A5B4FC;

            font-size: 12.5px;
            font-weight: 600;

            letter-spacing: 0.6px;
            text-transform: uppercase;
        }


        /* =====================================================
           BRAND TITLE
        ===================================================== */

        .brand-title {
            font-family: 'Sora', sans-serif;

            font-size: 50px;
            font-weight: 800;

            line-height: 1.08;

            margin-bottom: 18px;

            letter-spacing: -1.8px;

            color: #F8FAFC;
        }

        .brand-title span {

            background:
                linear-gradient(
                    135deg,
                    #818CF8 0%,
                    #C084FC 50%,
                    #F0ABFC 100%
                );

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;

            background-clip: text;
        }


        /* =====================================================
           BRAND SUBTITLE
        ===================================================== */

        .brand-subtitle {
            font-size: 21px;
            font-weight: 500;

            color: #CBD5E1;

            margin-bottom: 18px;
        }


        /* =====================================================
           BRAND DESCRIPTION
        ===================================================== */

        .brand-description {
            max-width: 470px;

            font-size: 15.5px;
            line-height: 1.75;

            color: #8B96AC;

            margin-bottom: 34px;
        }


        /* =====================================================
           FEATURES
        ===================================================== */

        .feature-grid {
            display: flex;
            flex-direction: column;

            gap: 4px;
        }

        .feature-item {

            display: flex;
            align-items: center;

            gap: 14px;

            padding: 12px 14px;
            margin: 4px 0;

            border-radius: 14px;

            color: #D7DEEA;

            font-size: 14.5px;
            font-weight: 500;

            transition:
                background 0.25s ease,
                transform 0.25s ease;
        }

        .feature-item:hover {

            background:
                rgba(129, 140, 248, 0.07);

            transform:
                translateX(4px);
        }


        /* =====================================================
           FEATURE ICON
        ===================================================== */

        .feature-icon {

            flex-shrink: 0;

            width: 38px;
            height: 38px;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 11px;

            background:
                linear-gradient(
                    135deg,
                    rgba(99, 102, 241, 0.2),
                    rgba(168, 85, 247, 0.14)
                );

            border:
                1px solid
                rgba(129, 140, 248, 0.25);

            font-size: 16px;
        }


        /* =====================================================
           STATS STRIP
        ===================================================== */

        .stats-strip {

            display: flex;

            gap: 30px;

            margin-top: 34px;

            padding-top: 26px;

            border-top:
                1px solid
                rgba(148, 163, 184, 0.12);
        }

        .stat-value {

            font-family: 'Sora', sans-serif;

            font-size: 22px;
            font-weight: 700;

            color: #F8FAFC;
        }

        .stat-label {

            font-size: 12px;

            color: #6B7690;

            margin-top: 2px;
        }


        /* =====================================================
           LOGIN CARD
        ===================================================== */

        .login-card {

            background:
                rgba(13, 18, 32, 0.85);

            border:
                1px solid
                rgba(148, 163, 184, 0.14);

            border-radius: 26px;

            padding: 46px 42px;

            box-shadow:
                0 30px 80px rgba(0, 0, 0, 0.5),
                inset 0 1px 0
                rgba(255, 255, 255, 0.04);

            backdrop-filter: blur(24px);

            animation:
                fadeSlideUp
                0.7s
                ease
                0.1s
                both;
        }


        /* =====================================================
           LOGIN ICON
        ===================================================== */

        .login-icon-badge {

            width: 56px;
            height: 56px;

            border-radius: 16px;

            background:
                linear-gradient(
                    135deg,
                    #6366F1,
                    #A855F7
                );

            display: flex;

            align-items: center;
            justify-content: center;

            font-size: 24px;

            margin:
                0 auto 20px auto;

            box-shadow:
                0 10px 30px
                rgba(99, 102, 241, 0.35);
        }


        /* =====================================================
           LOGIN TITLE
        ===================================================== */

        .login-title {

            text-align: center;

            font-family: 'Sora', sans-serif;

            font-size: 28px;
            font-weight: 750;

            color: #F8FAFC;

            margin-bottom: 6px;
        }


        /* =====================================================
           LOGIN SUBTITLE
        ===================================================== */

        .login-subtitle {

            text-align: center;

            font-size: 13.5px;

            color: #8B96AC;

            margin-bottom: 30px;
        }


        /* =====================================================
           INPUTS
        ===================================================== */

        .stTextInput label {

            color:
                #B6C0D4 !important;

            font-weight:
                600 !important;

            font-size:
                13px !important;

            letter-spacing:
                0.2px;

            text-transform:
                uppercase;
        }

        .stTextInput input {

            background:
                rgba(6, 10, 20, 0.75)
                !important;

            color:
                #F8FAFC
                !important;

            border:
                1px solid
                rgba(148, 163, 184, 0.18)
                !important;

            border-radius:
                12px
                !important;

            height:
                50px
                !important;

            padding:
                0 16px
                !important;

            font-size:
                15px
                !important;

            transition:
                all 0.2s ease
                !important;
        }

        .stTextInput input:focus {

            border:
                1px solid
                #818CF8
                !important;

            box-shadow:
                0 0 0 4px
                rgba(99, 102, 241, 0.15)
                !important;
        }

        .stTextInput input::placeholder {

            color:
                #4B5670
                !important;
        }


        /* =====================================================
           REMEMBER ME
        ===================================================== */

        .stCheckbox label p {

            color:
                #8B96AC
                !important;

            font-size:
                13.5px
                !important;
        }


        /* =====================================================
           SIGN IN BUTTON
        ===================================================== */

        .stButton > button {

            width: 100%;

            height: 52px;

            border-radius: 12px;

            border: none;

            background:
                linear-gradient(
                    135deg,
                    #6366F1,
                    #8B5CF6,
                    #A855F7
                );

            background-size:
                200% 100%;

            color: #FFFFFF;

            font-size: 15.5px;

            font-weight: 700;

            letter-spacing: 0.2px;

            transition:
                all 0.25s ease;

            box-shadow:
                0 10px 30px
                rgba(99, 102, 241, 0.3);
        }

        .stButton > button:hover {

            background-position:
                100% 0;

            transform:
                translateY(-2px);

            box-shadow:
                0 14px 36px
                rgba(99, 102, 241, 0.42);
        }

        .stButton > button:active {

            transform:
                translateY(0px);
        }


        /* =====================================================
           DIVIDER
        ===================================================== */

        .divider-row {

            display: flex;

            align-items: center;

            gap: 14px;

            margin:
                26px 0 20px 0;
        }

        .divider-line {

            flex: 1;

            height: 1px;

            background:
                rgba(148, 163, 184, 0.15);
        }

        .divider-text {

            font-size: 12px;

            color: #4B5670;

            font-weight: 500;
        }


        /* =====================================================
           SECURE TEXT
        ===================================================== */

        .secure-text {

            text-align: center;

            margin-top: 22px;

            color: #59637C;

            font-size: 12px;

            display: flex;

            align-items: center;

            justify-content: center;

            gap: 6px;
        }


        /* =====================================================
           ALERTS
        ===================================================== */

        div[data-testid="stAlert"] {

            border-radius:
                12px;
        }


        /* =====================================================
           MOBILE
        ===================================================== */

        @media (max-width: 768px) {

            .login-wrapper {

                margin:
                    20px auto;
            }

            .brand-section {

                padding:
                    20px
                    8px
                    30px
                    8px;

                text-align:
                    center;
            }

            .brand-title {

                font-size:
                    34px;
            }

            .brand-subtitle {

                font-size:
                    18px;
            }

            .brand-description {

                margin-left:
                    auto;

                margin-right:
                    auto;
            }

            .feature-item {

                justify-content:
                    center;
            }

            .stats-strip {

                justify-content:
                    center;
            }

            .login-card {

                padding:
                    32px
                    22px;
            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )


    # =========================================================
    # PAGE WRAPPER
    # =========================================================

    render_html(
        '<div class="login-wrapper">'
    )


    # =========================================================
    # TWO COLUMN LAYOUT
    # IMPORTANT: BOTH COLUMNS ARE AT SAME INDENTATION
    # =========================================================

    left_column, right_column = st.columns(
        [1.15, 0.85],
        gap="large"
    )


    # =========================================================
    # LEFT BRANDING SECTION
    # =========================================================

    with left_column:

        render_html(
            """
            <div class="brand-section">

                <div class="brand-badge">
                    ✦ AI-Powered Interview Preparation
                </div>

                <div class="brand-title">
                    AI Mock<br>
                    <span>Interview</span>
                </div>

                <div class="brand-subtitle">
                    Practice smarter. Interview better.
                </div>

                <div class="brand-description">
                    Prepare for your dream career with intelligent mock
                    interviews that simulate real-world technical and
                    professional interview experiences — powered by AI
                    that adapts to you.
                </div>

                <div class="feature-grid">

                    <div class="feature-item">
                        <div class="feature-icon">✦</div>
                        <div>
                            AI-powered interview questions
                        </div>
                    </div>

                    <div class="feature-item">
                        <div class="feature-icon">◈</div>
                        <div>
                            Instant performance evaluation
                        </div>
                    </div>

                    <div class="feature-item">
                        <div class="feature-icon">↻</div>
                        <div>
                            Intelligent follow-up questions
                        </div>
                    </div>

                    <div class="feature-item">
                        <div class="feature-icon">♙</div>
                        <div>
                            Personalized AI career coaching
                        </div>
                    </div>

                    <div class="feature-item">
                        <div class="feature-icon">▣</div>
                        <div>
                            Professional interview reports
                        </div>
                    </div>

                </div>

                <div class="stats-strip">

                    <div>
                        <div class="stat-value">
                            50K+
                        </div>

                        <div class="stat-label">
                            Interviews Simulated
                        </div>
                    </div>

                    <div>
                        <div class="stat-value">
                            4.9/5
                        </div>

                        <div class="stat-label">
                            User Rating
                        </div>
                    </div>

                    <div>
                        <div class="stat-value">
                            120+
                        </div>

                        <div class="stat-label">
                            Question Domains
                        </div>
                    </div>

                </div>

            </div>
            """
        )


    # =========================================================
    # RIGHT LOGIN SECTION
    # IMPORTANT: THIS MUST BE OUTSIDE with left_column
    # =========================================================

    with right_column:

        render_html(
            """
            <div class="login-card">

                <div class="login-icon-badge">
                    🔐
                </div>

                <div class="login-title">
                    Welcome Back
                </div>

                <div class="login-subtitle">
                    Sign in to continue your interview preparation
                </div>

            </div>
            """
        )


        # =====================================================
        # EMAIL
        # =====================================================

        email = st.text_input(
            "Email Address",
            key="login_email",
            placeholder="Enter your email"
        )


        # =====================================================
        # PASSWORD
        # =====================================================

        password = st.text_input(
            "Password",
            type="password",
            key="login_password",
            placeholder="Enter your password"
        )


        # =====================================================
        # REMEMBER ME
        # =====================================================

        remember_col, _ = st.columns(
            [1, 1]
        )

        with remember_col:

            st.checkbox(
                "Remember me",
                key="login_remember_me"
            )


        render_html(
            "<div style='height: 6px'></div>"
        )


        # =====================================================
        # LOGIN BUTTON
        # =====================================================

        if st.button(
            "Sign In",
            key="login_button",
            use_container_width=True
        ):

            if not email.strip():

                st.warning(
                    "Please enter your email address."
                )

            elif not password.strip():

                st.warning(
                    "Please enter your password."
                )

            else:

                with st.spinner(
                    "Signing you in..."
                ):

                    user = login(
                        email.strip(),
                        password
                    )


                if user:

                    login_user(
                        user
                    )

                    st.success(
                        f"Welcome back, {user['name']}!"
                    )

                    st.rerun()

                else:

                    st.error(
                        "Invalid email or password."
                    )


        # =====================================================
        # SECURE ACCESS
        # =====================================================

        render_html(
            """
            <div class="divider-row">

                <div class="divider-line"></div>

                <div class="divider-text">
                    SECURE ACCESS
                </div>

                <div class="divider-line"></div>

            </div>

            <div class="secure-text">
                🔒 Your data is encrypted and protected
            </div>
            """
        )


    # =========================================================
    # CLOSE PAGE WRAPPER
    # =========================================================

    render_html(
        "</div>"
    )