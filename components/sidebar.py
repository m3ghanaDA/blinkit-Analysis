import streamlit as st

def sidebar(df):

    st.sidebar.header("Filters")

    location = st.sidebar.selectbox(
        "Outlet Location",
        ["All"] + sorted(df["Outlet Location Type"].unique().tolist())
    )

    size = st.sidebar.selectbox(
        "Outlet Size",
        ["All"] + sorted(df["Outlet Size"].unique().tolist())
    )

    item = st.sidebar.selectbox(
        "Item Type",
        ["All"] + sorted(df["Item Type"].unique().tolist())
    )

    return location, size, item