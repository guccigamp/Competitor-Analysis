import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
df = pd.read_csv("datasets/companies_locations.csv")
secret_access_token = os.getenv("secret_access_token")
free_access_token = os.getenv("free_access_token")

"""
Returns a scattergeo figure of all companies' warehouse locations 
"""
def all_companies_scattergeo():
    fig = go.Figure()

    for company in df.company.unique():
        fig.add_trace(go.Scattermapbox(
            mode="markers", 
            lat=df.query(f"company == '{company}'")["latitude"],
            lon=df.query(f"company == '{company}'")["longitude"], 
            text=df.query(f"company == '{company}'")["text"],
            name=company,
            opacity=0.7,
            marker=dict(
                # symbol="marker",
                size=15,
                color=df.query(f"company == '{company}'")["color"]
            )
        ))
        
    fig.update_mapboxes(accesstoken=free_access_token) 

    fig.update_layout(
        title = 'Location of All Companies<br>(Hover for info)',
        height=600,
        mapbox=dict(
            style='open-street-map',
            zoom=3,
            center=dict(lon=df['longitude'].mean(), lat=df['latitude'].mean())
        ),
        template="plotly_dark"
    ) 

    return fig




def filter_by_company_scattergeo(selected_companies):
    fig = go.Figure()

    for company in selected_companies:
        fig.add_trace(go.Scattermapbox(
            mode="markers", 
            lat=df.query(f"company == '{company}'")["latitude"],
            lon=df.query(f"company == '{company}'")["longitude"], 
            text=df.query(f"company == '{company}'")["text"],
            name=company,
            opacity=0.7,
            marker=dict(
                # symbol="marker",
                size=15,
                color=df.query(f"company == '{company}'")["color"]
            )
        ))
        
    fig.update_mapboxes(accesstoken=free_access_token) 

    fig.update_layout(
        title = 'Location of Selected Companies<br>(Hover for info)',
        height=600,
        mapbox=dict(
            style='open-street-map',
            zoom=3,
            center=dict(lon=df['longitude'].mean(), lat=df['latitude'].mean())
        ),
        template="plotly_dark"
    ) 

    return fig


