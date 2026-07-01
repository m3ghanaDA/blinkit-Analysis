import streamlit as st

from utils.data_loader import load_data
from utils.preprocessing import preprocess_data

from style.styles import load_css

from components.header import show_header
from components.sidebar import sidebar

from utils.metrics import calculate_metrics

from charts.fat_content import create_fat_content_chart
from charts.fat_by_outlet import create_fat_by_outlet
from charts.item_type import create_item_type_chart
from charts.outlet_establishment import create_outlet_establishment_chart
from charts.outlet_size import create_outlet_size_chart
from charts.outlet_location import create_outlet_location_chart

from components.outlet_table import outlet_summary



st.set_page_config(
    page_title="BlinkIt Analysis Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

df = preprocess_data(load_data())

show_header()

location, size, item = sidebar(df)

metrics = calculate_metrics(df)
#metrics = calculate_metrics(filtered_df)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- KPI ROW ----------

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        label="💰 Total Sales",
        value=f"${metrics['total_sales']/1_000_000:.2f}M"
    )

with k2:
    st.metric(
        label="📈 Average Sales",
        value=f"${metrics['avg_sales']:.0f}"
    )

with k3:
    st.metric(
        label="📦 No. of Items",
        value=f"{metrics['items']:}"
    )

with k4:
    st.metric(
        label="⭐ Average Rating",
        value=f"{metrics['rating']:.1f}"
    )

#st.divider()

st.markdown("<br>", unsafe_allow_html=True)


row1_col1, row1_col2 = st.columns([1,2])

with row1_col1:

    with st.container(border=True):

        st.plotly_chart(
            create_fat_content_chart(df),
            use_container_width=True,
            config={"displayModeBar": False}
        )

with row1_col2:

    with st.container(border=True):

        st.plotly_chart(
            create_fat_by_outlet(df),
            use_container_width=True,
            config={"displayModeBar": False}
        )



row2_col1, row2_col2 = st.columns([1,1])

with row2_col1:
    with st.container(border=True):
        st.plotly_chart(
            create_item_type_chart(df),
            use_container_width=True,
            config={"displayModeBar": False}
        )

with row2_col2:
    with st.container(border=True):
        st.plotly_chart(
            create_outlet_establishment_chart(df),
            use_container_width=True,
            config={"displayModeBar": False}
        )




row3_col1, row3_col2 = st.columns(2)

with row3_col1:
    with st.container(border=True):
        st.plotly_chart(
            create_outlet_size_chart(df),
            use_container_width=True,
            config={"displayModeBar": False}
        )

with row3_col2:
    with st.container(border=True):
        st.plotly_chart(
            create_outlet_location_chart(df),
            use_container_width=True,
            config={"displayModeBar": False}
        )


with st.container(border=True):

    st.subheader("Outlet Type")

    outlet_summary(df)