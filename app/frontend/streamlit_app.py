import streamlit as st
from pathlib import Path
import time

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
    [
        "💡 Validate Idea",
        "🆚 Compare Ideas"
    ]
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

            sample_result = {

                "score": 82,

                "demand": "High",

                "risks": [
                    "Strong competition in the market",
                    "Customer acquisition cost may be high",
                    "User adoption challenge in early stages"
                ],

                "improvements": [
                    "Focus on a niche audience initially",
                    "Create a strong referral strategy",
                    "Integrate WhatsApp for engagement",
                    "Launch MVP before scaling"
                ],

                "metrics": {
                    "Feasibility": 82,
                    "Uniqueness": 75,
                    "Demand": 91,
                    "Scalability": 86,
                    "Innovation": 80
                }
            }

            render_results_panel(
                sample_result
            )

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
    unsafe_allow_html=True
)