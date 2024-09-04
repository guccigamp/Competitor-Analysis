from dash import Dash
import dash_bootstrap_components as dbc


# Creating an Instance of the app
app = Dash(
    external_stylesheets=[dbc.themes.DARKLY, "/assets/dropdown.css"],
    assets_folder="assets"
    )




