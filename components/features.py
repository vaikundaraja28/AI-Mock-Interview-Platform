import streamlit as st


def features():

    st.markdown("## 🔥 Features")

    c1, c2, c3, c4 = st.columns(4)

    cards = [
        ("🧠", "AI Interview"),
        ("📄", "Resume Review"),
        ("🎤", "Voice Analysis"),
        ("📊", "Performance Analytics")
    ]

    for col, (icon, title) in zip([c1, c2, c3, c4], cards):
        with col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <h2>{icon}</h2>
                    <p><b>{title}</b></p>
                </div>
                """,
                unsafe_allow_html=True
            )