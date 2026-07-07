import streamlit as st
from services.auth_service import login
from auth.session import login_user


def login_page():

    st.markdown("## 🔐 Login")

    email = st.text_input(
        "📧 Email",
        key="login_email"
    )

    password = st.text_input(
        "🔒 Password",
        type="password",
        key="login_password"
    )

    if st.button(
        "Login",
        key="login_button",
        use_container_width=True
    ):

        user = login(email, password)

        if user:

            login_user(user)

            st.success(f"Welcome {user['name']}!")

            st.rerun()

        else:

            st.error("Invalid email or password.")