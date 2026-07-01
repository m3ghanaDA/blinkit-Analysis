def apply_chart_theme(fig):

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(
            family="Arial",
            size=13,
            color="#333333"
        ),
        title_font=dict(
            size=18
        ),
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )
    )

    fig.update_xaxes(showgrid=False)

    fig.update_yaxes(showgrid=True, gridcolor="#EEEEEE")

    return fig