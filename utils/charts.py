import plotly.express as px
import streamlit as st


def fat_content_chart(df):

    sales = (
        df.groupby("Item Fat Content")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        sales,
        values="Sales",
        names="Item Fat Content",
        hole=0.55,
        title="Sales by Fat Content"
    )

    fig.update_traces(textposition="inside")

    st.plotly_chart(fig, use_container_width=True)


def item_type_chart(df):

    sales = (
            df.groupby("Item Type")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

    fig = px.bar(
            sales,
            x="Sales",
            y="Item Type",
            orientation="h",
            title="Sales by Item Type"
        )

    fig.update_layout(
        yaxis={'categoryorder':'total ascending'}
        )

    st.plotly_chart(fig, use_container_width=True)


def outlet_establishment_chart(df):

    sales = (
        df.groupby("Outlet Establishment Year")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        sales,
        x="Outlet Establishment Year",
        y="Sales",
        markers=True,
        title="Outlet Establishment"
    )

    st.plotly_chart(fig, use_container_width=True)


    
def outlet_size_chart(df):

    sales = (
        df.groupby("Outlet Size")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        sales,
        x="Outlet Size",
        y="Sales",
        title="Sales by Outlet Size"
    )

    st.plotly_chart(fig, use_container_width=True)



def outlet_location_chart(df):

    sales = (
        df.groupby("Outlet Location Type")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        sales,
        x="Outlet Location Type",
        y="Sales",
        color="Outlet Location Type",
        title="Sales by Outlet Location"
    )

    st.plotly_chart(fig, use_container_width=True)



def outlet_type_chart(df):

    sales = (
        df.groupby("Outlet Type")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        sales,
        x="Sales",
        y="Outlet Type",
        orientation="h",
        title="Sales by Outlet Type"
    )

    st.plotly_chart(fig, use_container_width=True)