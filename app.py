from dash import Dash, html, dcc
from dash import Input, Output, callback
from dash._callback import PreventUpdate
import plotly.express as px
import pandas as pd

companies_df = pd.read_csv("Comp Analysis- BI Report.csv")

def all_companies_scatter_map():
    fig = px.scatter_mapbox(
        data_frame=companies_df,
        lat="latitude", lon="longitude",
        title="Locations of our Competitor's Warehouses",
        color="top_competitors",
        hover_name="top_competitors",
        hover_data={
            "city": True,
            "state": True,
            "top_competitors": False,
            "latitude": False,
            "longitude": False
        },
        labels={"top_competitors": "Our Top Competitors"}
    )

    fig.update_layout(mapbox_style="open-street-map", mapbox_zoom=4,
        margin={"r":2,"t":2,"l":2,"b":2}) 

    fig.update_traces(cluster=dict(enabled=True))
    return fig

app = Dash()


app.layout = html.Div([
    html.H1("Dashboard To view our Top Competitor's Warehouse", style={"textAlign":"center"}),
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
                multi=True
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

    fig = px.scatter_mapbox(
        data_frame=companies_df.query("top_competitors in @company"),
        # data_frame=competitor_df,
        lat="latitude", lon="longitude",
        title="Locations of @company",
        color="top_competitors",
        hover_name="top_competitors",
        hover_data={
            "city": True,
            "state": True,
            "top_competitors": False,
            "latitude": False,
            "longitude": False
        },
        labels={"top_competitors": "Our Top Competitors"}
    )

    fig.update_layout(mapbox_style="open-street-map", mapbox_zoom=4,
        margin={"r":2,"t":2,"l":2,"b":2}) 
    
    fig.update_traces(cluster=dict(enabled=True))

    return fig

app.run_server(debug=True)