import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

def load_app2(pass_val):
    layout = html.Div([
        html.H3('App 2'),
        dcc.Dropdown(
            id='app-2-dropdown',
            options=[
                {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
                    'NYC', 'MTL', 'LA', pass_val, pass_val
                ]
            ]
        ),
        html.Div(id='app-2-display-value'),
        dcc.Link('Go to App 2', href='/apps/app2')
    ])

    return layout


@app.callback(
    Output('app-2-display-value', 'children'),
    [Input('app-2-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)