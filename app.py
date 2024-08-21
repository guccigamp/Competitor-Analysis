from dash import Dash, html, dcc
from dash import Input, Output, callback
from dash._callback import PreventUpdate
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as  dbc

companies_df = pd.read_csv("Comp Analysis- BI Report.csv")
df = pd.read_csv("companies_locations.csv")

def all_companies_scatter_map():
    # Create a plotly figure
    fig = go.Figure()

    # Looping thru all the company names
    for company in df.company.unique():
        # Adding traces by company
        fig.add_trace(go.Scattergeo(
            locationmode="USA-states",
            lat=df.query(f"company == '{company}'")["latitude"], lon=df.query(f"company == '{company}'")["longitude"],
            text=df.query(f"company == '{company}'")["text"], mode="markers",
            marker = dict(
                size=15,
                symbol=6,
            ), name=company
        ))

    fig.update_layout(
        title = 'Location of All Companies<br>(Hover for info)',
        geo_scope='usa', height=600
        
    )

    return fig

    return fig

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Top Competitors", style={"textAlign":"center"}),
    html.Div(
        id='View All',
        children=[
            dcc.Graph(
                id="view-all-scatter-map", 
                figure=all_companies_scatter_map()
            )        
        ]
    ),
    html.Div(
        id="view-by-company",
        children=[
            dcc.Dropdown(
                id='company-dropdown',
                options=companies_df.top_competitors.unique(),
                multi=True,
                style={"textAlign":"center"},

            ),
            dcc.Graph(id='view-by-company-scatter-map')
        ]
    )
])



    

# Callback function that updates the Map by the selected company
@callback(
    Output(component_id="view-by-company-scatter-map", component_property="figure"),
    Input(component_id="company-dropdown", component_property="value")
)
def update_map_by_company(company):
    if not company:
        raise PreventUpdate

    

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050)
