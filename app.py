import streamlit as st

from database.database import initialize
from core.theme import load_theme

from auth.session import initialize_session
from auth.login import login_page
from auth.register import register_page

from pages.dashboard import dashboard
from resume.upload import upload_resume

st.set_page_config(
    page_title="AI Mock Interview",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------
# Initialize
# ----------------------------

initialize()
initialize_session()

# ----------------------------
# Login / Register
# ----------------------------

if not st.session_state.logged_in:

    option = st.radio(
    "Choose an option",
    ["Login", "Register"],
    horizontal=True,
    label_visibility="collapsed"

    )

    st.write("")

    if option == "Login":
        login_page()
    else:
        register_page()

    st.stop()

# ----------------------------
# Logged In Area
# ----------------------------

load_theme()

page = st.session_state.page

if page == "dashboard":

    dashboard()

elif page == "resume":

    upload_resume()

else:

    dashboard()