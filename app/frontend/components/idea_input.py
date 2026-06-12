import streamlit as st


def render_idea_input():
    st.subheader("💡 Enter Your Startup Idea")

    idea = st.text_area(
        "Describe your idea",
        height=200,
        placeholder="""
Example:

An AI assistant that helps students find internships
based on skills, interests and real-time opportunities.
""",
    )

    return idea
