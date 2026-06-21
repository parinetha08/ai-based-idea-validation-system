"""Results panel UI for displaying idea analysis."""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from app.frontend.components.score_card import render_score_card


# -----------------------------
# KPI SECTION
# -----------------------------
def render_kpis(text, score, demand_value):
    """Render KPI cards."""

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        render_score_card(text["score"], str(score))

    with c2:
        demand_map = {
            "high": text["high"],
            "medium": text["medium"],
            "low": text["low"],
        }
        render_score_card(text["demand"], demand_map.get(demand_value, text["low"]))

    with c3:
        risk = (
            text["low"]
            if score >= 80
            else text["medium"]
            if score >= 70
            else text["high"]
        )
        render_score_card(text["risk"], risk)

    with c4:
        scale = "90%" if score >= 80 else "75%" if score >= 70 else "60%"
        render_score_card(text["scale"], scale)


# -----------------------------
# CHARTS SECTION
# -----------------------------
def render_charts(result, text, score):
    """Render charts section."""

    st.subheader("🎯 " + text["overall_score"])

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": text["idea_score"]},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#EFFF00"},
                "steps": [
                    {"range": [0, 50], "color": "#ef4444"},
                    {"range": [50, 75], "color": "#f59e0b"},
                    {"range": [75, 100], "color": "#22c55e"},
                ],
            },
        )
    )

    st.plotly_chart(gauge, use_container_width=True)

    metrics = result.get("metrics", {})
    keys = list(metrics.keys())
    values = list(metrics.values())

    radar = go.Figure()

    radar.add_trace(
        go.Scatterpolar(
            r=values,
            theta=keys,
            fill="toself",
            name=text["report"],
            line={"color": "#EFFF00"},
        )
    )

    radar.update_layout(
        polar={"radialaxis": {"visible": True, "range": [0, 100]}},
        showlegend=False,
        height=500,
    )

    st.plotly_chart(radar, use_container_width=True)

    df = pd.DataFrame(
        {
            text["metric"]: keys,
            text["score"]: values,
        }
    )

    fig = px.bar(df, x=text["metric"], y=text["score"], text=text["score"])
    st.plotly_chart(fig, use_container_width=True)


# -----------------------------
# RISKS SECTION
# -----------------------------
def render_risks(text, risks, improvements):
    """Render risks and improvements."""

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚠️ " + text["risks"])
        for r in risks:
            st.error(r)

    with col2:
        st.subheader("✨ " + text["recommendations"])
        for i in improvements:
            st.success(i)


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def render_results_panel(result, text):
    """Render complete results dashboard."""

    st.markdown("## 📊 " + text["report"])

    score = result.get("score", 0)
    demand_value = result.get("demand", "low").lower()

    # FIX: safe argument unpacking (prevents pylint E1121 issues)
    render_kpis(text, score, demand_value)
    render_charts(result, text, score)
    render_risks(text, result.get("risks", []), result.get("improvements", []))

    st.markdown("---")

    if score >= 90:
        st.success(text["exceptional"])
    elif score >= 80:
        st.success(text["strong"])
    elif score >= 70:
        st.warning(text["promising"])
    else:
        st.error(text["high_risk"])

    st.markdown("---")

    st.subheader("💰 " + text["investor_recommendation"])

    if score >= 85:
        st.success(text["investable"])
    elif score >= 70:
        st.warning(text["conditional"])
    else:
        st.error(text["not_recommended"])

    st.subheader("🤖 " + text["ai_confidence"])

    confidence = min(score + 10, 95)
    st.progress(confidence)
    st.caption(f"{confidence}% {text['confidence_caption']}")

    st.markdown("---")

    report = f"""
AI IDEA VALIDATION REPORT

Score: {score}
Demand: {demand_value}
"""

    st.download_button(
        "📄 " + text["download_report"],
        report,
        file_name="startup_report.txt",
    )
