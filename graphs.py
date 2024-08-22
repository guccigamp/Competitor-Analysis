import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("datasets/companies_locations.csv")

"""
Returns a scattergeo figure of all companies' warehouse locations 
"""
def all_companies_scattergeo():
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




def filter_by_company_scattergeo(selected_companies):
    fig = go.Figure()
    for company in selected_companies:
        fig.add_trace(go.Scattergeo(
            locationmode="USA-states",
            lat=df.query(f"company == '{company}'")["latitude"],
            lon=df.query(f"company == '{company}'")["longitude"],
            text=df.query(f"company == '{company}'")["text"],
            mode="markers",
            marker=dict(
                size=15,
                symbol=6,
            ),
            name=company
        ))

    fig.update_layout(
        title='Location of Selected Companies<br>(Hover for info)',
        geo_scope='usa',
    )

    return fig