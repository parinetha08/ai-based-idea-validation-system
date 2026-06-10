import streamlit as st
import pandas as pd

from components.score_card import render_score_card


def render_results_panel(result):

    st.divider()

    col1, col2 = st.columns([1, 2])

    with col1:
        render_score_card(result["score"])

        st.metric(
            "Market Demand",
            result["demand"]
        )

    with col2:
        st.subheader("⚠ Risks")

        for risk in result["risks"]:
            st.warning(risk)

        st.subheader("✨ Suggestions")

        for suggestion in result["improvements"]:
            st.success(suggestion)

    st.subheader("📊 Idea Breakdown")

    chart_data = pd.DataFrame(
        result["metrics"].items(),
        columns=["Metric", "Score"]
    )

    st.bar_chart(
        chart_data.set_index("Metric")
    )