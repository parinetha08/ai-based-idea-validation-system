import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from components.score_card import metric_card


def render_results_panel(result):
    st.markdown("## 📊 Startup Validation Report")

    # Get score first
    score = result["score"]

    # -----------------------------
    # KPI CARDS (BRIGHT + CLEAN)
    # -----------------------------
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("SCORE", f"{score}")

    with c2:
        metric_card("DEMAND", result["demand"])

    with c3:
        if score >= 80:
            risk_level = "Low"
        elif score >= 70:
            risk_level = "Medium"
        else:
            risk_level = "High"

        metric_card("RISK", risk_level)

    with c4:
        if score >= 80:
            scale = "90%"
        elif score >= 70:
            scale = "75%"
        else:
            scale = "60%"

        metric_card("SCALE", scale)

    st.markdown("---")

    # -----------------------------
    # SCORE LOGIC
    # -----------------------------
    if score >= 90:
        st.success("🔥 Exceptional startup opportunity")
    elif score >= 80:
        st.success("🚀 Strong startup potential")
    elif score >= 70:
        st.warning("📈 Promising but needs refinement")
    else:
        st.error("⚠️ High-risk concept")

    st.markdown("---")

    # -----------------------------
    # GAUGE CHART
    # -----------------------------
    st.subheader("🎯 Overall Validation Score")

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "Idea Score"},
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

    # -----------------------------
    # RADAR
    # -----------------------------
    st.subheader("🕸 Startup Strength Radar")

    metrics = list(result["metrics"].keys())
    values = list(result["metrics"].values())

    radar = go.Figure()

    radar.add_trace(
        go.Scatterpolar(
            r=values,
            theta=metrics,
            fill="toself",
            name="Idea",
            line=dict(color="#EFFF00"),
        )
    )

    radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False,
        height=500,
    )

    st.plotly_chart(radar, use_container_width=True)

    # -----------------------------
    # BAR CHART
    # -----------------------------
    st.subheader("📈 Detailed Analytics")

    df = pd.DataFrame(
        {
            "Metric": metrics,
            "Score": values,
        }
    )

    fig = px.bar(df, x="Metric", y="Score", text="Score")

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # -----------------------------
    # RISKS & IMPROVEMENTS
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚠️ Risks")
        for risk in result["risks"]:
            st.error(risk)

    with col2:
        st.subheader("✨ Recommendations")
        for item in result["improvements"]:
            st.success(item)

    st.markdown("---")

    # -----------------------------
    # INVESTOR VIEW
    # -----------------------------
    st.subheader("💰 Investor Recommendation")

    if score >= 85:
        st.success("✅ INVESTABLE — Strong market potential")
    elif score >= 70:
        st.warning("🟡 CONDITIONAL — Needs refinement")
    else:
        st.error("🔴 NOT RECOMMENDED")

    # -----------------------------
    # AI CONFIDENCE
    # -----------------------------
    st.subheader("🤖 AI Confidence")

    confidence = min(score + 10, 95)

    st.progress(confidence)
    st.caption(f"{confidence}% confidence based on evaluation signals.")

    st.markdown("---")

    # -----------------------------
    # DOWNLOAD
    # -----------------------------
    report = f"""
AI IDEA VALIDATION REPORT

Score: {score}
Demand: {result["demand"]}
Risk: {risk_level}
Scale: {scale}

Risks:
{chr(10).join(result["risks"])}

Improvements:
{chr(10).join(result["improvements"])}
"""

    st.download_button(
        "📄 Download Report",
        report,
        file_name="startup_report.txt",
    )
