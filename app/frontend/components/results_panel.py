import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from components.score_card import metric_card


def render_results_panel(result, text):
    st.markdown("## 📊 " + text["report"])

    # -----------------------------
    # GET SCORE
    # -----------------------------
    score = result["score"]

    # -----------------------------
    # KPI CARDS
    # -----------------------------
    c1, c2, c3, c4 = st.columns(4)

    # SCORE
    with c1:
        metric_card(text["score"], f"{score}")

    # DEMAND
    with c2:
        demand_value = result["demand"]

        if demand_value.lower() == "high":
            demand_value = text["high"]
        elif demand_value.lower() == "medium":
            demand_value = text["medium"]
        else:
            demand_value = text["low"]

        metric_card(text["demand"], demand_value)

    # RISK
    with c3:
        if score >= 80:
            risk_level = text["low"]
        elif score >= 70:
            risk_level = text["medium"]
        else:
            risk_level = text["high"]

        metric_card(text["risk"], risk_level)

    # SCALE
    with c4:
        if score >= 80:
            scale = "90%"
        elif score >= 70:
            scale = "75%"
        else:
            scale = "60%"

        metric_card(text["scale"], scale)

    st.markdown("---")

    # -----------------------------
    # SCORE LOGIC
    # -----------------------------
    if score >= 90:
        st.success(text["exceptional"])
    elif score >= 80:
        st.success(text["strong"])
    elif score >= 70:
        st.warning(text["promising"])
    else:
        st.error(text["high_risk"])

    st.markdown("---")

    # -----------------------------
    # GAUGE CHART
    # -----------------------------
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

    # -----------------------------
    # RADAR CHART
    # -----------------------------
    st.subheader("🕸 " + text["strength_radar"])

    metrics = list(result["metrics"].keys())
    values = list(result["metrics"].values())

    radar = go.Figure()

    radar.add_trace(
        go.Scatterpolar(
            r=values,
            theta=metrics,
            fill="toself",
            name=text["report"],
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
    st.subheader("📈 " + text["analytics"])

    df = pd.DataFrame(
        {
            text["metric"]: metrics,
            text["score"]: values,
        }
    )

    fig = px.bar(
        df,
        x=text["metric"],
        y=text["score"],
        text=text["score"],
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # -----------------------------
    # RISKS & IMPROVEMENTS
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚠️ " + text["risks"])

        for risk in result["risks"]:
            st.error(risk)

    with col2:
        st.subheader("✨ " + text["recommendations"])

        for item in result["improvements"]:
            st.success(item)

    st.markdown("---")

    # -----------------------------
    # INVESTOR RECOMMENDATION
    # -----------------------------
    st.subheader("💰 " + text["investor_recommendation"])

    if score >= 85:
        st.success(text["investable"])
    elif score >= 70:
        st.warning(text["conditional"])
    else:
        st.error(text["not_recommended"])

    # -----------------------------
    # AI CONFIDENCE
    # -----------------------------
    st.subheader("🤖 " + text["ai_confidence"])

    confidence = min(score + 10, 95)

    st.progress(confidence)
    st.caption(f"{confidence}% {text['confidence_caption']}")

    st.markdown("---")

    # -----------------------------
    # DOWNLOAD REPORT
    # -----------------------------
    report = f"""
AI IDEA VALIDATION REPORT

Score: {score}
Demand: {demand_value}
Risk: {risk_level}
Scale: {scale}

Risks:
{chr(10).join(result["risks"])}

Improvements:
{chr(10).join(result["improvements"])}
"""

    st.download_button(
        "📄 " + text["download_report"],
        report,
        file_name="startup_report.txt",
    )
