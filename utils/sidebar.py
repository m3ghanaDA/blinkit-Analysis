import streamlit as st

def sidebar_filters(df):

    st.sidebar.header("🔍 Filters")

    outlet_location = st.sidebar.multiselect(
        "Outlet Location",
        options=sorted(df["Outlet Location Type"].unique()),
        default=sorted(df["Outlet Location Type"].unique())
    )

    outlet_size = st.sidebar.multiselect(
        "Outlet Size",
        options=sorted(df["Outlet Size"].dropna().unique()),
        default=sorted(df["Outlet Size"].dropna().unique())
    )

    outlet_type = st.sidebar.multiselect(
        "Outlet Type",
        options=sorted(df["Outlet Type"].unique()),
        default=sorted(df["Outlet Type"].unique())
    )

    item_type = st.sidebar.multiselect(
        "Item Type",
        options=sorted(df["Item Type"].unique()),
        default=sorted(df["Item Type"].unique())
    )

    fat_content = st.sidebar.multiselect(
        "Fat Content",
        options=sorted(df["Item Fat Content"].unique()),
        default=sorted(df["Item Fat Content"].unique())
    )

    filtered_df = df[
        (df["Outlet Location Type"].isin(outlet_location)) &
        (df["Outlet Size"].isin(outlet_size)) &
        (df["Outlet Type"].isin(outlet_type)) &
        (df["Item Type"].isin(item_type)) &
        (df["Item Fat Content"].isin(fat_content))
    ]

    return filtered_df