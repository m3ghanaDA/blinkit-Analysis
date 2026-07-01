import plotly.graph_objects as go
from utils.chart_theme import apply_chart_theme


def create_outlet_establishment_chart(df):

    sales = (
        df.groupby("Outlet Establishment Year")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Outlet Establishment Year")
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=sales["Outlet Establishment Year"],
            y=sales["Sales"],
            mode="lines+markers",
            line=dict(color="#8DC63F", width=4),
            marker=dict(size=8),
        )
    )

    fig.update_layout(
        title="Outlet Establishment",
        height=500,
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=20, r=20, t=50, b=20),
        xaxis_title="",
        yaxis_title="Sales",
        showlegend=False
    )

    fig = apply_chart_theme(fig)

    return fig