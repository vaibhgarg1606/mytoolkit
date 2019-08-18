import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

def load_app1(global_data, pass_val):
    num_cols = len(global_data['csv_data'].columns.values)
    cols = 'num cols: {0}'.format(str(num_cols))
    layout = html.Div([
        html.H3('App 1'),
        dcc.Dropdown(
            id='app-1-dropdown',
            options=[
                {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                    'NYC', 'MTL', 'LA', pass_val, cols
                ]
            ]
        ),
        html.Div(id='app-1-display-value'),
        dcc.Link('Go to App 2', href='/apps/app2')
    ])

    return layout

@app.callback(
    Output('app-1-display-value', 'children'),
    [Input('app-1-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)