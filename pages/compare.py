import os
import sys
sys.path.append(os.path.abspath(""))

from dash import Dash, Input, Output, callback
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from components.navbar import navbar
from pages.graphs import compare_scattergeo
import pandas as pd

df = pd.read_csv(r"C:\Users\shaha\Development\Competitor Analysis\datasets\companies_locations.csv")    


layout = dbc.Container(
    [
        navbar,
        dbc.Form([
            dbc.Select(
                id="company-dropdown",
                options=df.query("company != 'Altor Solutions'").company.unique(),
                style={'margin-left': 'auto', 'margin-right': 'auto'},
                className="bg-black text-white",
                placeholder="Select Company Name",
            ),
            html.Div(id='compare-content')])
    ]
)

"""
This callback takes the values of "company-dropdown" as an input to refresh the graph of filtered companies
"""
@callback(
    Output('compare-content', 'children'),
    Input('company-dropdown', 'value'),
    suppress_callback_exceptions=True
)
def update_map(selected_companies):
    return dcc.Graph(id="compare-scattergeo",
                     figure=compare_scattergeo(selected_companies))


