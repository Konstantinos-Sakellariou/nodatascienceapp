from dash import html, dcc
import dash_bootstrap_components as dbc

eda_page = html.Div([
            html.H2("Automatic Exploratory Data Analysis"),
            html.P(
                "In this section we perform exploratory data analysis of all the features in the dataset,"
                " using the package pandas_profilling."),
            dbc.Button(children=[html.I(className="fa fa mr-2"), "Run EDA"],
                       id="second_step_eda",
                       className="mt-1"),
            html.Br(),
            html.Br(),
            dcc.Loading(children=[html.Div(id='automatic_eda', style={"margin-bottom": "10px"})],
                        type="dot", fullscreen=False)
        ]
        )