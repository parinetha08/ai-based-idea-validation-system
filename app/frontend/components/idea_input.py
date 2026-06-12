import streamlit as st


def render_idea_input(text):
    st.subheader("💡 " + text["enter_startup_idea"])

    idea = st.text_area(
        text["describe_idea"],
        height=200,
        placeholder=text["idea_placeholder"],
    )

    return idea
