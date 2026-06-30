import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    df = pd.read_excel("data/BlinkIT Grocery Data.xlsx")

    return df