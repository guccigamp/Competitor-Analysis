from dash import Dash, html, dcc
from dash import Input, Output, callback
from dash._callback import PreventUpdate
from graphs import all_companies_scattergeo
from graphs import filter_by_company_scattergeo
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import time
import dash_bootstrap_components as  dbc


# Read companies location dataset
df = pd.read_csv("datasets/companies_locations.csv")

# Creating an Instance of the app
app = Dash(
    external_stylesheets=[dbc.themes.FLATLY],
    assets_folder="assets"
    )

app.layout = dbc.Container(
    [
        html.H1("Top Competitors"),
        dbc.Tabs(
            [
                dbc.Tab(label="All Companies", tab_id="tab-1"),
                dbc.Tab(label="Filter by Company", tab_id="tab-2"),
            ],
            id="tabs",
            active_tab="tab-1",
        ),
        html.Div(id="tab-content", className="p-4")
    ]
)

"""
This callback takes the 'active_tab' property as input, as well as the
stored graphs, and renders the tab content depending on what the value of
'active_tab' is.
"""
@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "active_tab"),
)
def render_tab_content(active_tab):
    if active_tab == "tab-1":
        return dcc.Graph(id="all-company-scattergeo", figure=all_companies_scattergeo())
    elif active_tab == "tab-2":
        return dbc.Form([
            dcc.Dropdown(
                id='company-dropdown',
                options=df.company.unique(),
                multi=True,
                value=df.company.unique(),
                className="form-select-primary"
            ), 
            html.Div(id='filter-content')
            
            ])
    

"""
"""
@app.callback(
    Output('filter-content', 'children'),
    Input('company-dropdown', 'value'),
    suppress_callback_exceptions=True
)
def update_map(selected_companies):
    return dcc.Graph(id="filter-by-company-scattergeo", figure=filter_by_company_scattergeo(selected_companies))

# Append the necessary Bootstrap CSS files and the custom dropdown_css to the app's CSS using app.css.append_css().
    
if __name__ == "__main__":
    app.run_server(host="0.0.0.0",port=8050, dev_tools_ui=False, dev_tools_props_check=False)
