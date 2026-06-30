import plotly.graph_objects as go

def apply_glass_chart(fig):

    fig.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(255,255,255,.02)",

        font=dict(
            family="Segoe UI",
            color="white",
            size=13
        ),

        title_font=dict(
            size=24,
            color="white"
        ),

        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        ),

        legend=dict(

            bgcolor="rgba(0,0,0,0)",

            borderwidth=0,

            font=dict(
                color="white"
            )

        ),

        hoverlabel=dict(

            bgcolor="#1E293B",

            font=dict(
                color="white"
            )

        )

    )

    fig.update_xaxes(

        showgrid=False,

        zeroline=False,

        linecolor="rgba(255,255,255,.15)",

        tickfont=dict(color="#D8D8D8")

    )

    fig.update_yaxes(

        showgrid=True,

        gridcolor="rgba(255,255,255,.08)",

        zeroline=False,

        tickfont=dict(color="#D8D8D8")

    )

    return fig