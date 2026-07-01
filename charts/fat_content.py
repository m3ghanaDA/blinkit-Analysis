import plotly.graph_objects as go
from utils.chart_theme import apply_chart_theme


def create_fat_content_chart(df):

    sales = (
        df.groupby("Item Fat Content")["Sales"]
        .sum()
        .reset_index()
    )

    colors = ["#8BC34A", "#FFC107"]

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            labels=sales["Item Fat Content"],
            values=sales["Sales"],
            hole=0.6,
            marker=dict(colors=colors),
            textinfo="label+percent",
            hovertemplate="<b>%{label}</b><br>Sales: $%{value:,.0f}<extra></extra>"
        )
    )

    fig.update_layout(
        title="Fat Content",
        height=350,
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(
            orientation="h",
            y=-0.15
        )
    )

    fig = apply_chart_theme(fig)

    return fig