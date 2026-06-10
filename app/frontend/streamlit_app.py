import streamlit as st

from components.idea_input import render_idea_input
from components.results_panel import render_results_panel
from components.comparison_view import render_comparison_view

st.set_page_config(
    page_title="AI Idea Validator",
    page_icon="🚀",
    layout="wide"
)

# Load CSS
from pathlib import Path

css_path = Path(__file__).parent / "assets" / "styles.css"

with open(css_path, "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<div class='hero'>
    <h1>🚀 AI Idea Validator</h1>
    <p>Validate your startup ideas before building them.</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["💡 Validate Idea", "🆚 Compare Ideas"])

with tab1:
    idea = render_idea_input()

    if st.button("Analyze Idea", use_container_width=True):
        sample_result = {
            "score": 82,
            "demand": "High",
            "risks": [
                "Strong competition",
                "User adoption challenge"
            ],
            "improvements": [
                "Focus on niche users",
                "Add WhatsApp integration"
            ],
            "metrics": {
                "Feasibility": 80,
                "Uniqueness": 75,
                "Demand": 90,
                "Scalability": 85
            }
        }

        render_results_panel(sample_result)

with tab2:
    render_comparison_view()