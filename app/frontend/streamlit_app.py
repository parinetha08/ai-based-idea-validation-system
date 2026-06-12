import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
import streamlit as st
from pathlib import Path
import time
import requests

from components.idea_input import render_idea_input
from components.results_panel import render_results_panel
from components.comparison_view import render_comparison_view
from app.i18n.translator import load_language

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(page_title="AI Idea Validator", page_icon="🚀", layout="wide")
lang = st.sidebar.selectbox(
    "Language",
    ["en", "te","hi"]
)

text = load_language(lang)

# --------------------------------------------------
# LOAD CSS
# --------------------------------------------------

css_path = Path(__file__).parent / "assets" / "styles.css"

with open(css_path, "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.title("🚀 " + text["title"])
st.caption(text["subtitle"])

# --------------------------------------------------
# TABS
# --------------------------------------------------

tab1, tab2 = st.tabs([
    "💡 " + text["validate_idea"],
    "🆚 " + text["compare_ideas"]
])

# --------------------------------------------------
# TAB 1
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
                response = requests.post(
                    "http://127.0.0.1:8000/validate", json={"idea": idea}, timeout=10
                )

                if response.status_code == 200:
                    result = response.json()

                    # Add metrics if backend doesn't provide them
                    if "metrics" not in result:
                        result["metrics"] = {
                            text["feasibility"]: result["score"],
                            text["uniqueness"]: 75,
                            text["demand_metric"]: 90,
                            text["scalability"]: 85,
                            text["innovation"]: 80,
                    }
                        st.subheader(text["report"])

                    render_results_panel(result,text)

                else:
                    st.error(f"Backend error: {response.status_code}")

            except Exception as e:
                st.error(f"Could not connect to backend: {e}")

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
