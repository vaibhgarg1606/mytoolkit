import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
from apps import app1, app2, bivariate, home
import pandas as pd


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

global_data = {}

layout_csv = html.Div([
        html.Div([
            html.Label('CSV Path'),
            html.Br(),
            dcc.Input(id='input-box', type='text')
        ]),
        html.Button('Submit', id='button'),
        html.Div(id='output-container-button')
    ])

pass_val = 'Checking it on this'

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.load_app1(global_data, pass_val)
    elif pathname == '/apps/app2':
        return app2.load_app2(pass_val)
    elif pathname == '/apps/bivariate':
        return bivariate.load_app2(global_data)
    else:
        return layout_csv

@app.callback(
    Output(component_id='output-container-button', component_property='children'),
    [Input('button', 'n_clicks')],
    state=[State(component_id='input-box', component_property='value')]
)
def csv_stats(n_clicks, csv_path):
    try:
        df = pd.read_csv(csv_path)
        global_data['csv_data'] = df
        num_cols = len(df.columns.values)
        return ('Number of columns: {0}'.format(str(num_cols)))
    except:
        return ('Some error occured')

if __name__ == '__main__':
    app.run_server()