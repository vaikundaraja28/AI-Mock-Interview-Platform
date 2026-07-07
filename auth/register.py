import streamlit as st
from services.auth_service import register


def register_page():

    st.markdown("## 📝 Register")

    name = st.text_input(
        "👤 Full Name",
        key="register_name"
    )

    email = st.text_input(
        "📧 Email",
        key="register_email"
    )

    password = st.text_input(
        "🔒 Password",
        type="password",
        key="register_password"
    )

    if st.button(
        "Create Account",
        key="register_button",
        use_container_width=True
    ):

        if register(name, email, password):

            st.success("Account created successfully!")

        else:

            st.error("Email already exists.")