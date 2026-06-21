"""UI component for idea input form."""

import streamlit as st


def render_idea_input(text):
    """Render input form for user idea submission."""
    st.subheader("💡 " + text["enter_startup_idea"])

    idea = st.text_area(
        text["describe_idea"],
        height=200,
        placeholder=text["idea_placeholder"],
    )

    return idea
