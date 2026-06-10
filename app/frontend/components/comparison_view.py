import streamlit as st


def render_comparison_view():
    st.subheader("🆚 Compare Startup Ideas")

    col1, col2 = st.columns(2)

    with col1:
        st.text_area(
            "Idea 1",
            height=150,
            placeholder="Enter first startup idea...",
        )

    with col2:
        st.text_area(
            "Idea 2",
            height=150,
            placeholder="Enter second startup idea...",
        )

    st.button(
        "Compare Ideas",
        use_container_width=True,
    )
