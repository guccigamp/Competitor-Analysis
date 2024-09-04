import os
import sys

sys.path.append(os.path.abspath(""))

from dash import Dash, Input, Output, callback
from dash import html, dcc
import dash_bootstrap_components as dbc
from components.navbar import navbar
from pages.graphs import all_companies_scattergeo
import pandas as pd
import app

df = pd.read_csv("..\datasets\companies_locations.csv")


layout = dbc.Container(
    [
        navbar,
        dcc.Graph(id="all-company-scattergeo",
                          figure=all_companies_scattergeo())
    ]
)

