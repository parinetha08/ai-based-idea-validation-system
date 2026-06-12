import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))
import streamlit as st
from app.backend.services.idea_analyzer import analyze_idea


def render_comparison_view():
    st.subheader("🆚 Compare Startup Ideas")

    col1, col2 = st.columns(2)

    with col1:
        idea1 = st.text_area(
            "Idea 1",
            height=150,
            placeholder="Enter first startup idea...",
        )

    with col2:
        idea2 = st.text_area(
            "Idea 2",
            height=150,
            placeholder="Enter second startup idea...",
        )

    if st.button(
        "Compare Ideas",
        use_container_width=True,
    ):

        if not idea1.strip() or not idea2.strip():
            st.warning("Please enter both ideas.")

        else:
            result1 = analyze_idea(idea1)
            result2 = analyze_idea(idea2)

            st.markdown("### 📊 Comparison")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### Idea 1")
                st.metric("Score", result1["score"])
                st.metric("Demand", result1["demand"])

            with col2:
                st.markdown("#### Idea 2")
                st.metric("Score", result2["score"])
                st.metric("Demand", result2["demand"])

            if result1["score"] > result2["score"]:
                st.success("🏆 Idea 1 is stronger.")
            elif result2["score"] > result1["score"]:
                st.success("🏆 Idea 2 is stronger.")
            else:
                st.info("🤝 Both ideas are equally strong.")