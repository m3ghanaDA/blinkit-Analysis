import plotly.graph_objects as go
from utils.chart_theme import apply_chart_theme


def create_item_type_chart(df):

    sales = (
        df.groupby("Item Type")["Sales"]
        .sum()
        .sort_values(ascending=True)
        .reset_index()
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=sales["Sales"],
            y=sales["Item Type"],
            orientation="h",
            marker_color="#8DC63F",
            text=[f"${x/1000:.0f}K" for x in sales["Sales"]],
            textposition="outside"
        )
    )

    fig.update_layout(
        title="Item Type",
        height=500,
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=20, r=20, t=50, b=20),
        xaxis_title="Sales",
        yaxis_title="",
        showlegend=False
    )

    fig = apply_chart_theme(fig)


    return fig