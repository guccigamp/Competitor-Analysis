from dash import dcc, html
from dash.dependencies import Input, Output

from app import app
from pages import home, filters, compare

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', style={
        'margin': "0px",
        'padding': "0px"
    })
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home.layout
    elif pathname == '/filters':
        return filters.layout
    elif pathname == '/compare':
        return compare.layout
    else:
        return '404 Page Not Found'


# app.run_server(debug=True)
app.run_server(host="0.0.0.0",port=8050, dev_tools_ui=False, dev_tools_props_check=False)