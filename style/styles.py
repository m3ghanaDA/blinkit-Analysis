import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .main{
        background:#F5F5F5;
    }

    .block-container{
        padding-top:1rem;
        padding-left:2rem;
        padding-right:2rem;
        max-width:100%;
    }

    div[data-testid="stMetric"]{

        background:white;

        border-radius:15px;

        padding:18px;

        border:1px solid #ECECEC;

        box-shadow:0 2px 8px rgba(0,0,0,.08);

    }

    </style>
    """, unsafe_allow_html=True)