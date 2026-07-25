import streamlit as st

from services.auth_service import register


def render_html(html: str) -> None:
    """
    Render raw HTML safely using Streamlit.
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


def register_page():

    # =========================================================
    # PREMIUM REGISTER PAGE - CUSTOM CSS
    # =========================================================

    st.markdown(
        """
        <style>

        @import url(
            'https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap'
        );


        /* =====================================================
           GLOBAL
        ===================================================== */

        * {
            font-family:
                'Inter',
                -apple-system,
                sans-serif;
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

            background-attachment:
                fixed;
        }

        .block-container {

            padding-top:
                2rem;

            padding-bottom:
                2rem;

            max-width:
                1200px;
        }


        /* =====================================================
           ANIMATION
        ===================================================== */

        @keyframes fadeSlideUp {

            from {

                opacity:
                    0;

                transform:
                    translateY(18px);
            }

            to {

                opacity:
                    1;

                transform:
                    translateY(0);
            }

        }


        /* =====================================================
           MAIN WRAPPER
        ===================================================== */

        .register-wrapper {

            max-width:
                1160px;

            margin:
                50px auto 30px auto;

            padding:
                10px;
        }


        /* =====================================================
           LEFT BRANDING
        ===================================================== */

        .register-brand-section {

            padding:
                45px
                40px
                40px
                20px;

            color:
                #F8FAFC;

            animation:
                fadeSlideUp
                0.7s
                ease
                both;
        }


        /* =====================================================
           BADGE
        ===================================================== */

        .register-brand-badge {

            display:
                inline-flex;

            align-items:
                center;

            gap:
                8px;

            padding:
                9px 16px;

            margin-bottom:
                28px;

            background:
                linear-gradient(
                    135deg,
                    rgba(99, 102, 241, 0.18),
                    rgba(168, 85, 247, 0.14)
                );

            border:
                1px solid
                rgba(129, 140, 248, 0.35);

            border-radius:
                999px;

            color:
                #A5B4FC;

            font-size:
                12.5px;

            font-weight:
                600;

            letter-spacing:
                0.6px;

            text-transform:
                uppercase;
        }


        /* =====================================================
           TITLE
        ===================================================== */

        .register-brand-title {

            font-family:
                'Sora',
                sans-serif;

            font-size:
                48px;

            font-weight:
                800;

            line-height:
                1.08;

            margin-bottom:
                18px;

            letter-spacing:
                -1.8px;

            color:
                #F8FAFC;
        }

        .register-brand-title span {

            background:
                linear-gradient(
                    135deg,
                    #818CF8 0%,
                    #C084FC 50%,
                    #F0ABFC 100%
                );

            -webkit-background-clip:
                text;

            -webkit-text-fill-color:
                transparent;

            background-clip:
                text;
        }


        /* =====================================================
           SUBTITLE
        ===================================================== */

        .register-brand-subtitle {

            font-size:
                21px;

            font-weight:
                500;

            color:
                #CBD5E1;

            margin-bottom:
                18px;
        }


        /* =====================================================
           DESCRIPTION
        ===================================================== */

        .register-brand-description {

            max-width:
                470px;

            font-size:
                15.5px;

            line-height:
                1.75;

            color:
                #8B96AC;

            margin-bottom:
                34px;
        }


        /* =====================================================
           BENEFITS
        ===================================================== */

        .register-benefit-list {

            display:
                flex;

            flex-direction:
                column;

            gap:
                10px;
        }


        .register-benefit {

            display:
                flex;

            align-items:
                center;

            gap:
                14px;

            padding:
                11px 14px;

            border-radius:
                14px;

            color:
                #D7DEEA;

            font-size:
                14.5px;

            font-weight:
                500;

            transition:
                background 0.25s ease,
                transform 0.25s ease;
        }


        .register-benefit:hover {

            background:
                rgba(129, 140, 248, 0.07);

            transform:
                translateX(4px);
        }


        /* =====================================================
           BENEFIT ICON
        ===================================================== */

        .register-benefit-icon {

            flex-shrink:
                0;

            width:
                38px;

            height:
                38px;

            display:
                flex;

            align-items:
                center;

            justify-content:
                center;

            border-radius:
                11px;

            background:
                linear-gradient(
                    135deg,
                    rgba(99, 102, 241, 0.2),
                    rgba(168, 85, 247, 0.14)
                );

            border:
                1px solid
                rgba(129, 140, 248, 0.25);

            font-size:
                16px;
        }


        /* =====================================================
           REGISTER CARD
        ===================================================== */

        .register-card {

            background:
                rgba(13, 18, 32, 0.88);

            border:
                1px solid
                rgba(148, 163, 184, 0.14);

            border-radius:
                26px;

            padding:
                42px;

            box-shadow:

                0 30px 80px
                rgba(0, 0, 0, 0.5),

                inset
                0 1px 0
                rgba(255, 255, 255, 0.04);

            backdrop-filter:
                blur(24px);

            animation:
                fadeSlideUp
                0.7s
                ease
                0.1s
                both;
        }


        /* =====================================================
           REGISTER ICON
        ===================================================== */

        .register-icon-badge {

            width:
                56px;

            height:
                56px;

            border-radius:
                16px;

            background:
                linear-gradient(
                    135deg,
                    #6366F1,
                    #A855F7
                );

            display:
                flex;

            align-items:
                center;

            justify-content:
                center;

            font-size:
                24px;

            margin:
                0 auto 20px auto;

            box-shadow:
                0 10px 30px
                rgba(99, 102, 241, 0.35);
        }


        /* =====================================================
           REGISTER TITLE
        ===================================================== */

        .register-title {

            text-align:
                center;

            font-family:
                'Sora',
                sans-serif;

            font-size:
                28px;

            font-weight:
                750;

            color:
                #F8FAFC;

            margin-bottom:
                6px;
        }


        /* =====================================================
           REGISTER SUBTITLE
        ===================================================== */

        .register-subtitle {

            text-align:
                center;

            font-size:
                13.5px;

            color:
                #8B96AC;

            margin-bottom:
                28px;
        }


        /* =====================================================
           INPUT LABELS
        ===================================================== */

        .stTextInput label {

            color:
                #B6C0D4
                !important;

            font-weight:
                600
                !important;

            font-size:
                13px
                !important;

            letter-spacing:
                0.2px;

            text-transform:
                uppercase;
        }


        /* =====================================================
           INPUT FIELDS
        ===================================================== */

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
           CREATE ACCOUNT BUTTON
        ===================================================== */

        .stButton > button {

            width:
                100%;

            height:
                52px;

            border-radius:
                12px;

            border:
                none;

            background:
                linear-gradient(
                    135deg,
                    #6366F1,
                    #8B5CF6,
                    #A855F7
                );

            background-size:
                200% 100%;

            color:
                #FFFFFF;

            font-size:
                15.5px;

            font-weight:
                700;

            letter-spacing:
                0.2px;

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
                translateY(0);
        }


        /* =====================================================
           DIVIDER
        ===================================================== */

        .register-divider {

            display:
                flex;

            align-items:
                center;

            gap:
                14px;

            margin:
                24px 0 18px 0;
        }


        .register-divider-line {

            flex:
                1;

            height:
                1px;

            background:
                rgba(148, 163, 184, 0.15);
        }


        .register-divider-text {

            font-size:
                12px;

            color:
                #4B5670;

            font-weight:
                500;
        }


        /* =====================================================
           SECURITY TEXT
        ===================================================== */

        .register-secure-text {

            text-align:
                center;

            color:
                #59637C;

            font-size:
                12px;

            margin-top:
                20px;

            line-height:
                1.6;
        }


        /* =====================================================
           SUCCESS / ERROR ALERT
        ===================================================== */

        div[data-testid="stAlert"] {

            border-radius:
                12px;
        }


        /* =====================================================
           MOBILE
        ===================================================== */

        @media (max-width: 768px) {

            .register-wrapper {

                margin:
                    20px auto;
            }

            .register-brand-section {

                padding:
                    20px
                    8px
                    30px
                    8px;

                text-align:
                    center;
            }

            .register-brand-title {

                font-size:
                    34px;
            }

            .register-brand-subtitle {

                font-size:
                    18px;
            }

            .register-brand-description {

                margin-left:
                    auto;

                margin-right:
                    auto;
            }

            .register-benefit {

                justify-content:
                    center;
            }

            .register-card {

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
        '<div class="register-wrapper">'
    )


    # =========================================================
    # TWO COLUMN LAYOUT
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
            <div class="register-brand-section">

                <div class="register-brand-badge">
                    ✦ Start Your AI Interview Journey
                </div>

                <div class="register-brand-title">
                    Build Your<br>
                    <span>Interview Edge</span>
                </div>

                <div class="register-brand-subtitle">
                    Prepare smarter. Grow with confidence.
                </div>

                <div class="register-brand-description">
                    Create your account and unlock personalized
                    AI-powered interview preparation designed to help
                    you practice, improve, and perform with confidence.
                </div>

                <div class="register-benefit-list">

                    <div class="register-benefit">

                        <div class="register-benefit-icon">
                            ✦
                        </div>

                        <div>
                            Personalized AI mock interviews
                        </div>

                    </div>


                    <div class="register-benefit">

                        <div class="register-benefit-icon">
                            ◈
                        </div>

                        <div>
                            Instant feedback on your performance
                        </div>

                    </div>


                    <div class="register-benefit">

                        <div class="register-benefit-icon">
                            ↻
                        </div>

                        <div>
                            Adaptive follow-up questions
                        </div>

                    </div>


                    <div class="register-benefit">

                        <div class="register-benefit-icon">
                            ♙
                        </div>

                        <div>
                            AI-powered career guidance
                        </div>

                    </div>


                    <div class="register-benefit">

                        <div class="register-benefit-icon">
                            ▣
                        </div>

                        <div>
                            Track your interview progress
                        </div>

                    </div>

                </div>

            </div>
            """
        )


    # =========================================================
    # RIGHT REGISTER CARD
    # =========================================================

    with right_column:

        render_html(
            """
            <div class="register-card">

                <div class="register-icon-badge">
                    🚀
                </div>

                <div class="register-title">
                    Create Your Account
                </div>

                <div class="register-subtitle">
                    Start preparing for your next interview today
                </div>

            </div>
            """
        )


        # =====================================================
        # FULL NAME
        # =====================================================

        name = st.text_input(
            "Full Name",
            key="register_name",
            placeholder="Enter your full name"
        )


        # =====================================================
        # EMAIL
        # =====================================================

        email = st.text_input(
            "Email Address",
            key="register_email",
            placeholder="Enter your email address"
        )


        # =====================================================
        # PASSWORD
        # =====================================================

        password = st.text_input(
            "Password",
            type="password",
            key="register_password",
            placeholder="Create a strong password"
        )


        # =====================================================
        # CONFIRM PASSWORD
        # =====================================================

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            key="register_confirm_password",
            placeholder="Re-enter your password"
        )


        render_html(
            "<div style='height: 8px'></div>"
        )


        # =====================================================
        # CREATE ACCOUNT
        # =====================================================

        if st.button(
            "Create Account",
            key="register_button",
            use_container_width=True
        ):

            if not name.strip():

                st.warning(
                    "Please enter your full name."
                )

            elif not email.strip():

                st.warning(
                    "Please enter your email address."
                )

            elif not password.strip():

                st.warning(
                    "Please create a password."
                )

            elif len(password) < 6:

                st.warning(
                    "Password must be at least 6 characters."
                )

            elif password != confirm_password:

                st.warning(
                    "Passwords do not match."
                )

            else:

                with st.spinner(
                    "Creating your account..."
                ):

                    account_created = register(
                        name.strip(),
                        email.strip(),
                        password
                    )


                if account_created:

                    st.success(
                        "Account created successfully!"
                    )

                else:

                    st.error(
                        "An account with this email already exists."
                    )


        # =====================================================
        # DIVIDER
        # =====================================================

        render_html(
            """
            <div class="register-divider">

                <div class="register-divider-line"></div>

                <div class="register-divider-text">
                    SECURE REGISTRATION
                </div>

                <div class="register-divider-line"></div>

            </div>

            <div class="register-secure-text">
                🔒 Your account information is securely protected
                <br>
                Start your AI-powered interview preparation journey.
            </div>
            """
        )


    # =========================================================
    # CLOSE PAGE WRAPPER
    # =========================================================

    render_html(
        "</div>"
    )