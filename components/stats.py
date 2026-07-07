import streamlit as st


def stats():

    col1, col2, col3 = st.columns(3)

    stats_data = [
        ("1200+", "Interviews"),
        ("91%", "Average Score"),
        ("530+", "Students")
    ]

    for col, (number, title) in zip([col1, col2, col3], stats_data):

        with col:

            st.markdown(
                f"""
                <div class="metric-card">
                    <h2>{number}</h2>
                    <p>{title}</p>
                </div>
                """,
                unsafe_allow_html=True
            )