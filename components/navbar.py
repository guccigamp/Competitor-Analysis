import dash_bootstrap_components as dbc
from dash import Input, Output, callback, callback_context
from dash import Dash, html



ALTOR_LOGO = "../assets/Altor-Logo_Bob_PNG.png"

navmenu = dbc.Row(
    [
        dbc.Col(
            dbc.DropdownMenu(
                label="Visuals",
                children=[
                    dbc.DropdownMenuItem("All Companies", href="/"),
                    dbc.DropdownMenuItem("Filters", href="filters"),
                    dbc.DropdownMenuItem("Compare", href="/compare"),
                ],
                direction="start"
            )
        ),
    ],
    align="center",
)


navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=ALTOR_LOGO, height=50)),
                        dbc.Col(dbc.NavbarBrand("Top Competitors", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.Row([navmenu])
        ]
    ),
    color="black",
    dark=True,
)