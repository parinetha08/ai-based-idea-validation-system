import streamlit as st
import pandas as pd
import plotly.express as px

from components.score_card import metric_card


def render_results_panel(result):

    st.divider()

    st.markdown("## 📊 Validation Report")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("Score", f"{result['score']}/100", "🚀")

    with c2:
        metric_card("Demand", result["demand"], "📈")

    with c3:
        metric_card("Risk", "Medium", "⚠️")

    with c4:
        metric_card("Scale", "85%", "🌍")

    st.markdown("---")

    st.subheader("📈 Idea Analytics")

    df = pd.DataFrame({
        "Metric": list(result["metrics"].keys()),
        "Score": list(result["metrics"].values())
    })

    fig = px.bar(
        df,
        x="Metric",
        y="Score",
        text="Score",
        title="Startup Evaluation Metrics"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("⚠ Risks")

        for risk in result["risks"]:
            st.error(risk)

    with col2:

        st.subheader("✨ Recommendations")

        for item in result["improvements"]:
            st.success(item)

    st.markdown("---")

    st.subheader("💰 Investor View")

    if result["score"] >= 80:
        st.success(
            "Strong startup potential. Worth further validation."
        )

    elif result["score"] >= 60:
        st.warning(
            "Promising but needs refinement."
        )

    else:
        st.error(
            "High risk idea. Needs significant improvement."
        )

    report = f"""
AI IDEA VALIDATION REPORT

Score: {result['score']}
Demand: {result['demand']}

Risks:
{chr(10).join(result['risks'])}

Suggestions:
{chr(10).join(result['improvements'])}
"""

    st.download_button(
        "📄 Download Report",
        report,
        file_name="idea_report.txt"
    )