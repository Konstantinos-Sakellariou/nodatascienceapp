from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc

import base64
import pandas as pd
from io import StringIO, BytesIO

from assets.code.config import datasets

upload_page = html.Div(
            [html.H2("Upload your dataset!"),
             html.P("Note that only csv and excel files are currently supported. It is wise to use a file"
                    " which is less than 2MB, so that the app can quickly perform any kind of calculations."),
             html.P(
                 "In this section you can quickly upload your dataset"
                 " and create interactive plots using the Graph area."),
             dcc.Upload(
                 id='upload-data',
                 children=html.Div([
                     'Drag and Drop or ',
                     html.A('Select Files')
                 ]),
                 style={
                     'width': '100%',
                     'height': '80%',
                     'lineHeight': '60px',
                     'borderWidth': '1px',
                     'borderStyle': 'dashed',
                     'borderRadius': '5px',
                     'textAlign': 'center',
                     'margin': '10',
                     'margin-top': "10px",
                     'margin-bottom': "20px"
                 },
                 # Allow multiple files to be uploaded
                 multiple=True
             ),
             html.P("Or you can choose one from the pre-loaded datasets to see the app in action."),
             html.Div([dcc.Dropdown(id='preloaded_dataset',
                                    # options=[{'label': i, 'value': i} for i in datasets],
                                    options=datasets,
                                    placeholder='Select your preloaded dataset...',
                                    style={"background-color": "#CAECD8", "width": "100%"},
                                    multi=False,
                                    persistence=True,
                                    persistence_type='session')],
                      style={"background-color": "white", "width": "35%"}),
             html.Br(),
             html.Div(id='output-data-upload', hidden=False)
             ]
        )


def return_output_data(df, filename):
    return html.Div([
        html.H5(filename),

        html.Hr(),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
            page_size=10,
            editable=True,
            row_deletable=True,
            style_cell=dict(textAlign='center'),
            style_header=dict(backgroundColor="#CAECD8"),
            style_data=dict(backgroundColor="lavender"),
            style_table={"height": "375px", "width": "400", 'overflowY': 'auto'},
            filter_action='native',
            sort_action='native',
            sort_mode='single',
            persistence=True,
            persistence_type="session"
        ),
        html.Div([
            html.Hr(),
            html.H3("Graph Area"),
            html.Hr()],
            style={
                'textAlign': 'center',
                "background-color": "white",
                "border-color": "white",
                "border-style": "solid"
            }
        ),
        html.P("Select feature name for the X-axis", style={"fontSize": "20px", }),
        dcc.Dropdown(id='xaxis-data',
                     options=[{'label': x, 'value': x} for x in df.columns],
                     style={"width": "50%"}),
        html.Br(),
        html.P("Select feature name for the Y-axis", style={"fontSize": "20px", }),
        dcc.Dropdown(id='yaxis-data',
                     options=[{'label': x, 'value': x} for x in df.columns],
                     style={"width": "50%"}),
        html.Br(),
        html.P("Select type of plot:", style={"fontSize": "20px", }),
        dcc.RadioItems(id='plot_type',
                       options=["  Bar Plot", "  Scatter Plot", "  Histogram (only x-axis feature)"],
                       value="  Bar Plot",
                       inline=False,
                       labelStyle={"display": "block"},
                       style={"width": "50%"}),
        html.Br(),
        dbc.Button(children=[html.I(className="fa fa mr-2"), "Create Graph"],
                   id="submit-button",
                   className="mt-1"
                   ),
        html.Hr(),
        html.Div(id='output-div'),
    ])


def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return return_output_data(df, filename)


def parse_contents_df(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return df.to_dict('records')
