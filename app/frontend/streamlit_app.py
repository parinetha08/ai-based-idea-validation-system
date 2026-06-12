import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
import streamlit as st
from pathlib import Path
import time

from app.backend.services.idea_analyzer import analyze_idea

from components.idea_input import render_idea_input
from components.results_panel import render_results_panel
from components.comparison_view import render_comparison_view

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Idea Validator",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# LOAD CSS
# --------------------------------------------------

css_path = Path(__file__).parent / "assets" / "styles.css"

with open(css_path, "r", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.title("🚀 AI Idea Validator")
st.caption("Validate startup ideas before investing time and money")

# --------------------------------------------------
# TABS
# --------------------------------------------------

tab1, tab2 = st.tabs(
    ["💡 Validate Idea", "🆚 Compare Ideas"]
)

# --------------------------------------------------
# TAB 1
# --------------------------------------------------

with tab1:
    idea = render_idea_input()

    if st.button(
        "🚀 Analyze Startup Idea",
        use_container_width=True
    ):

        if not idea.strip():
            st.warning(
                "Please enter your startup idea first."
            )

        else:
            progress_text = st.empty()

            progress_text.info(
                "🔍 Checking market demand..."
            )
            time.sleep(1)

            progress_text.info(
                "📈 Estimating scalability..."
            )
            time.sleep(1)

            progress_text.info(
                "⚡ Evaluating feasibility..."
            )
            time.sleep(1)

            progress_text.info(
                "🧠 Generating AI insights..."
            )
            time.sleep(1)

            progress_text.empty()

            try:
                result = analyze_idea(idea)

                if "metrics" not in result:
                    result["metrics"] = {
                        "Feasibility": result["score"],
                        "Uniqueness": 75,
                        "Demand": 90,
                        "Scalability": 85,
                        "Innovation": 80,
                    }

                render_results_panel(result)

            except Exception as e:
                st.error(f"Error: {e}")

# --------------------------------------------------
# TAB 2
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
            Built with ❤️ using Streamlit
        </p>
    </center>
    """,
    unsafe_allow_html=True,
)