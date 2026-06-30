import streamlit as st

from utils.data_loader import load_data
from utils.preprocessing import preprocess_data

st.set_page_config(
    page_title="BlinkIt Analytics",
    layout="wide"
)

st.title("🛒 BlinkIt Analytics Dashboard")

df = load_data()
df = preprocess_data(df)

st.write(df.head())


st.subheader("Dataset Information")

col1, col2, col3 = st.columns(3)

col1.metric("Rows", len(df))
col2.metric("Columns", len(df.columns))
col3.metric("Duplicates", df.duplicated().sum())

st.subheader("Missing Values")

st.dataframe(df.isnull().sum())