import streamlit as st

def render_score_card(score):
    st.markdown(
        f"""
        <div class='score-card'>
            <h1>{score}</h1>
            <p>Idea Score</p>
        </div>
        """,
        unsafe_allow_html=True
    )