import streamlit as st


def initialize_session():

    # Login Session

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "user" not in st.session_state:
        st.session_state.user = None

    if "page" not in st.session_state:
        st.session_state.page = "dashboard"

    # ==========================
    # Interview Session
    # ==========================

    if "current_question" not in st.session_state:
        st.session_state.current_question = 1

    if "total_questions" not in st.session_state:
        st.session_state.total_questions = 5

    if "scores" not in st.session_state:
        st.session_state.scores = []

    if "evaluations" not in st.session_state:
        st.session_state.evaluations = []

    if "questions" not in st.session_state:
        st.session_state.questions = []

    if "answers" not in st.session_state:
        st.session_state.answers = []


def login_user(user):

    st.session_state.logged_in = True
    st.session_state.user = user
    st.session_state.page = "dashboard"

    # Reset Interview Session

    st.session_state.current_question = 1
    st.session_state.scores = []
    st.session_state.evaluations = []
    st.session_state.questions = []
    st.session_state.answers = []


def logout():

    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.page = "dashboard"

    # Clear Interview Session

    st.session_state.current_question = 1
    st.session_state.scores = []
    st.session_state.evaluations = []
    st.session_state.questions = []
    st.session_state.answers = []

    st.rerun()