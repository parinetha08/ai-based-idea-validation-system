"""Score card UI component."""

import streamlit as st


def render_score_card(label: str, value):
    """Render score card UI."""
    st.metric(label=label, value=value)
