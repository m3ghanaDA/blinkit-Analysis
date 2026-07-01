import plotly.graph_objects as go
from utils.chart_theme import apply_chart_theme


def create_outlet_location_chart(df):

    sales = (
        df.groupby("Outlet Location Type")["Sales"]
        .sum()
        .sort_values(ascending=True)
        .reset_index()
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=sales["Sales"],
            y=sales["Outlet Location Type"],
            orientation="h",
            marker_color="#8BC34A",
            text=[f"${x/1000:.0f}K" for x in sales["Sales"]],
            textposition="outside"
        )
    )

    fig.update_layout(
        title="Outlet Location",
        height=360,
        showlegend=False
    )

    fig = apply_chart_theme(fig)

    return fig