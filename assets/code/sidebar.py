import dash_bootstrap_components as dbc
from dash import html

from assets.code.config import SIDEBAR_STYLE

sidebar = html.Div(
    [
        html.H2("Actions", className="display-4"),
        html.Hr(),
        html.P("A list of actions to complete a data science project without any knowledge on the data field",
               className="lead"),
        dbc.Nav(
            [
                html.Hr(),
                dbc.NavLink("Home - Documentation", href="/", active="exact"),
                html.Hr(),
                dbc.NavLink("Upload your Dataset", href="/upload_page", active="exact"),
                dbc.NavLink("Automatic Exploratory Data Analysis", href="/eda_page", active="exact"),
                dbc.NavLink("Data Modelling Options", href="/modelling_page", active="exact", id="datamodeloption"),
                dbc.NavLink("Download Options", href="/download_page", active="exact"),
                dbc.NavLink("What's next?", href="/whatsnext_page", active="exact", id="whatisnext", n_clicks=0),
                html.Hr(),
                html.Div(
                    [dbc.Button(children=[html.Span([html.Div("Contact",
                                                              style={"display": "inline-block"}),
                                                     html.I(className="fa-brands fa-github",
                                                            style={"display": "inline-block",
                                                                   "background-color": "black",
                                                                   "color": "black"})])],
                                id="open",
                                style={'width': '100%'}),
                     dbc.Modal(
                         [dbc.ModalHeader("E-mail"),
                          dbc.ModalBody("nodatascienceapp@gmail.com"),
                          dbc.ModalFooter(dbc.Button("CLOSE", id="close", className="ml-auto"))],
                         id="modal")]
                ),
                html.Br(),
                html.Div(
                    [
                        html.A(dbc.Button(children=[html.I(className="fa-brands fa-github", style={"color": "black"}),
                                                    "GitHub"], id="opengit", style={'width': '100%'}),
                               target="_blank",
                               href="https://github.com/Konstantinos-Sakellariou")]
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
