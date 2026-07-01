import streamlit as st

def show_header():

    col1, col2 = st.columns([1,5])

    with col1:
        st.image("assets/blinkitLOGO.png", width=100)

    with col2:

        st.markdown(
            """
            # BlinkIt

            ### India's last minute app
            """
        )

    st.divider()