import streamlit as st

def show_kpis(df):

    total_sales = df["Sales"].sum()
    avg_sales = df["Sales"].mean()
    total_items = len(df)
    avg_rating = df["Rating"].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
    col2.metric("📈 Average Sales", f"${avg_sales:.2f}")
    col3.metric("📦 Total Items", total_items)
    col4.metric("⭐ Average Rating", f"{avg_rating:.2f}")