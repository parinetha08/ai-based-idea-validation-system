"""Main Streamlit application entry point for AI Idea Validation System."""

import time
from pathlib import Path

import streamlit as st

from app.backend.services.idea_analyzer import analyze_idea
from app.i18n.translator import load_language
from app.frontend.components.idea_input import render_idea_input
from app.frontend.components.results_panel import render_results_panel
from app.frontend.components.comparison_view import render_comparison_view

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Idea Validator",
    page_icon="🚀",
    layout="wide",
)

# --------------------------------------------------
# LANGUAGE SELECTION
# --------------------------------------------------

lang = st.sidebar.selectbox("Language", ["en", "te", "hi"])
text = load_language(lang)

# --------------------------------------------------
# AI SETTINGS
# --------------------------------------------------

st.sidebar.markdown("---")
st.sidebar.subheader("🤖 AI Settings")

provider = st.sidebar.selectbox("AI Provider", ["Gemini", "Ollama"])

API_KEY = None

if provider == "Gemini":
    API_KEY = st.sidebar.text_input(
        "Gemini API Key (BYOK)",
        type="password",
        help="Enter your own Gemini API key",
    )
else:
    st.sidebar.success("Using Local Ollama Model")

# --------------------------------------------------
# LOAD CSS
# --------------------------------------------------

css_path = Path(__file__).parent / "assets" / "styles.css"

with open(css_path, encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.title("🚀 " + text["title"])
st.caption(text["subtitle"])

# --------------------------------------------------
# TABS
# --------------------------------------------------

tab1, tab2 = st.tabs(
    [
        "💡 " + text["validate_idea"],
        "🆚 " + text["compare_ideas"],
    ]
)

# --------------------------------------------------
# TAB 1 - IDEA VALIDATION
# --------------------------------------------------

with tab1:
    idea = render_idea_input(text)

    if st.button("🚀 " + text["analyze"], use_container_width=True):
        if not idea.strip():
            st.warning(text["enter_idea"])

        else:
            progress_text = st.empty()

            progress_text.info(text["checking_demand"])
            time.sleep(1)

            progress_text.info(text["estimating_scale"])
            time.sleep(1)

            progress_text.info(text["evaluating_feasibility"])
            time.sleep(1)

            progress_text.info(text["generating_insights"])
            time.sleep(1)

            progress_text.empty()

            try:
                st.write("Calling analyze_idea...")

                result = analyze_idea(
                    idea=idea,
                    provider=provider,
                    api_key=API_KEY or "",
                )

                # Fallback metrics if backend doesn't provide them
                if "metrics" not in result:
                    result["metrics"] = {
                        text["feasibility"]: result.get("score", 80),
                        text["uniqueness"]: 75,
                        text["demand_metric"]: 90,
                        text["scalability"]: 85,
                        text["innovation"]: 80,
                    }

                st.subheader(text["report"])
                render_results_panel(result, text)

                if "ai_analysis" in result:
                    st.subheader("🤖 AI Analysis")
                    st.write(result["ai_analysis"])

            except (ValueError, KeyError) as e:
                st.error(f"Analysis failed: {str(e)}")

# --------------------------------------------------
# TAB 2 - COMPARISON
# --------------------------------------------------

with tab2:
    render_comparison_view()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown(
    """
    <center>
        <p style="color:#94A3B8;">
            🚀 AI-Based Idea Validation System
            <br>
            Supports Gemini BYOK + Local Ollama
        </p>
    </center>
    """,
    unsafe_allow_html=True,
)
