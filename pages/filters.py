import os
import sys

sys.path.append(os.path.abspath(""))

import dash_bootstrap_components as dbc
import pandas as pd
from dash import Input, Output, callback
from dash import Dash, html, dcc

from pages.graphs import filter_by_company_scattergeo

from components.navbar import navbar

df = pd.read_csv("..\datasets\companies_locations.csv")

layout = dbc.Container(
    [
        navbar,
        dbc.Form([
            dcc.Dropdown(
                id='company-dropdown',
                options=df.company.unique(),
                multi=True,
                value=df.company.unique(),
                className="dbc"
            ),
            html.Div(id='filter-content')])
    ]
)

"""
This callback takes the values of "company-dropdown" as an input to refresh the graph of filtered companies
"""


@callback(
    Output('filter-content', 'children'),
    Input('company-dropdown', 'value'),
    suppress_callback_exceptions=True
)
def update_map(selected_companies):
    return dcc.Graph(id="filter-by-company-scattergeo",
                     figure=filter_by_company_scattergeo(selected_companies))

