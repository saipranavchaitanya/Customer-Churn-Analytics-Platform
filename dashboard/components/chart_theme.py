def apply_glass_chart(fig):

    fig.update_layout(

        template="plotly_dark",

        # Remove any undefined title
        title=None,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Segoe UI",
            size=13,
            color="white"
        ),

        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),

        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        ),

        hoverlabel=dict(
            bgcolor="#1E293B",
            font=dict(color="white")
        )
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(255,255,255,.08)",
        zeroline=False
    )

    return fig