import streamlit as st

def render_comparison_view():

    st.subheader("🆚 Compare Two Ideas")

    col1, col2 = st.columns(2)

    with col1:
        idea1 = st.text_area(
            "Idea 1",
            height=150,
            key="idea1"
        )

    with col2:
        idea2 = st.text_area(
            "Idea 2",
            height=150,
            key="idea2"
        )

    if st.button("Compare Ideas"):

        comparison = {
            "Idea 1": 76,
            "Idea 2": 88
        }

        st.bar_chart(comparison)