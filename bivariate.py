import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import BytesIO
import base64

from app import app
from apps.dash_utils import fig_to_uri
from __main__ import *

bivariate_data = {}

def load_app2(global_data):

    global bivariate_data
    bivariate_data = global_data

    print(global_data.keys())

    cols = global_data['csv_data'].columns.values
    layout = html.Div([
        # dcc.Input(id='plot_title', value='Type title...', type="text"),
        # dcc.Slider(
        #     id='box_size',
        #     min=1,
        #     max=10,
        #     value=4,
        #     step=1,
        #     marks=list(range(0, 10))
        # ),

        html.H3('Select Cols'),
        dcc.Dropdown(
            id='col1',
            options=[{'label': '{}'.format(i), 'value': i} for i in cols]
        ),

        dcc.Dropdown(
            id='col2',
            options=[{'label': '{}'.format(i), 'value': i} for i in cols]
        ),
        html.Button('Submit', id='button1'),
        html.Div([html.Img(id = 'cur_plot', src = '')],
                 id='plot_div')
    ])

    return layout


@app.callback(
    Output(component_id='cur_plot', component_property='src'),
    [Input('button1', 'n_clicks')],
    state=[State(component_id='col1', component_property='value'), State(component_id = 'col2', component_property='value')]
)
def update_graph(n_clicks, col1, col21):
    df = bivariate_data['csv_data']

    # print(global_data.keys())

    fig = plt.figure()
    # df = pd.read_csv('data.csv')

    if (not((col1 is None) | (col21 is None))):
        plt.plot(df[col1], df[col21])
    
    out_url = fig_to_uri(fig)
    return out_url