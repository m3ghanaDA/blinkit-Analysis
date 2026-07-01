import streamlit as st


def outlet_summary(df):

    summary = (
        df.groupby("Outlet Type")
        .agg(
            Total_Sales=("Sales", "sum"),
            Avg_Sales=("Sales", "mean"),
            Items=("Sales", "count"),
            Avg_Rating=("Rating", "mean"),
            Visibility=("Item Visibility", "mean")
        )
        .reset_index()
    )

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )