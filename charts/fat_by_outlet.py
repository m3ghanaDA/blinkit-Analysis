import plotly.graph_objects as go
from utils.chart_theme import apply_chart_theme


def create_fat_by_outlet(df):

    data = (
        df.groupby(
            ["Outlet Location Type", "Item Fat Content"]
        )["Sales"]
        .sum()
        .reset_index()
    )

    low = data[data["Item Fat Content"] == "Low Fat"]

    regular = data[data["Item Fat Content"] == "Regular"]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            y=low["Outlet Location Type"],
            x=low["Sales"],
            orientation="h",
            name="Low Fat",
            marker_color="#8BC34A"
        )
    )

    fig.add_trace(
        go.Bar(
            y=regular["Outlet Location Type"],
            x=regular["Sales"],
            orientation="h",
            name="Regular",
            marker_color="#FFC107"
        )
    )

    fig.update_layout(

        title="Fat by Outlet",

        barmode="stack",

        height=350,

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        ),

        legend=dict(
            orientation="h",
            y=-0.15
        )
    )


    fig = apply_chart_theme(fig)

    return fig