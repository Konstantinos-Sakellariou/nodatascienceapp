from dash import html, dcc
import dash_bootstrap_components as dbc
from assets.code.config import ml_types

modelling_page = html.Div([
            html.H2("Modelling Section"),
            html.P(
                "In this section the user can specify the type of the problem"
                " (either Classification or Regression), along with the target variable and"
                " get the best performing model."),
            html.P("In addition the user can compare all models on the data table provided below"),
            html.P("Now choose the type of the problem!"),
            html.Div([dcc.Dropdown(id='ml_type',
                                   options=[{'label': i, 'value': i} for i in ml_types],
                                   value='classification',
                                   style={"background-color": "#CAECD8", "width": "100%"},
                                   multi=False,
                                   persistence=True,
                                   persistence_type='session')],
                     style={"background-color": "white", "width": "20%"}),
            html.Br(),
            html.Br(),
            dbc.Button(children=[html.I(className="fa fa mr-2"),
                                 "First retrieve feature names and then choose you target variable"],
                       id="choose_target",
                       className="mt-1"
                       ),
            html.P("ONLY after retrieving the feature names you can choose your target variable!"),
            html.Div([dcc.Dropdown(id='target',
                                   options=[],
                                   value='Line',
                                   style={"background-color": "#CAECD8", "width": "100%"},
                                   multi=False,
                                   persistence=True,
                                   persistence_type='session'),
                      ], style={"background-color": "white", "width": "20%"}),
            html.Br(),
            html.Br(),
            dbc.Button(children=[html.I(className="fa fa mr-2"), "Run Data Modelling"],
                       id="third_step_modelling",
                       className="mt-1",
                       n_clicks=0
                       ),
            html.Br(),
            html.Br(),
            dcc.Loading(children=[html.Div(id='automatic_modelling')], type="cube", fullscreen=False),
        ])
