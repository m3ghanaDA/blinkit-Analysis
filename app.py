import streamlit as st
from utils.data_loader import load_data
from utils.sidebar import sidebar_filters
from utils.kpi import show_kpis
from utils.preprocessing import preprocess_data
from utils.charts import *

st.set_page_config(
    page_title="BlinkIT Analytics Dashboard",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 BlinkIT Analytics Dashboard")

df = load_data()
df = preprocess_data(df)

filtered_df = sidebar_filters(df)

show_kpis(filtered_df)

st.divider()

#st.dataframe(filtered_df)

col1, col2 = st.columns(2)

with col1:
    fat_content_chart(filtered_df)

with col2:
    item_type_chart(filtered_df)

col3, col4 = st.columns(2)

with col3:
    outlet_establishment_chart(filtered_df)

with col4:
    outlet_size_chart(filtered_df)

col5, col6 = st.columns(2)

with col5:
    outlet_location_chart(filtered_df)

with col6:
    outlet_type_chart(filtered_df)