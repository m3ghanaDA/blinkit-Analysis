import plotly.graph_objects as go
from utils.chart_theme import apply_chart_theme


def create_outlet_size_chart(df):

    data = (
        df.groupby("Outlet Size")["Sales"]
        .sum()
        .reset_index()
    )

    colors = [
        "#8BC34A",
        "#FFC107",
        "#4CAF50"
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            labels=data["Outlet Size"],
            values=data["Sales"],
            hole=0.55,
            marker=dict(colors=colors),
            textinfo="label+percent"
        )
    )

    fig.update_layout(
        title="Outlet Size",
        height=360
    )

    fig = apply_chart_theme(fig)

    return fig