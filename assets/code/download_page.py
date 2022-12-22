from dash import html, dcc
import dash_bootstrap_components as dbc
import os


download_page = html.Div([
            html.H2("Download the best model"),
            html.P(
                "By clicking on the download button below you can download the best"
                " available model for you machine learning problem."),
            html.P("Currently the only supported file option of downloading the model is a .joblib file"),
            html.Br(),
            dbc.Row(children=[
                dbc.Col(children=[
                    html.H6("Select your model to download"),
                    html.Div([dcc.Dropdown(id='models',
                                           placeholder="Select your model...",
                                           options=[{'label': i, 'value': i} for i in os.listdir("assets/models")],
                                           style={"background-color": "#CAECD8", "width": "100%"},
                                           multi=False,
                                           persistence=True,
                                           persistence_type='session'),
                              ], style={"background-color": "white", "width": "100%"}),
                    html.Br(),
                    dbc.Button(children=[html.I(className="fa-cloud-download"), "Download Model"],
                               id="fourth_step_model_download",
                               #className="mt-1"
                               className="fa-cloud-download"
                               ),
                    dcc.Download(id="download-model"),
                ]),
                dbc.Col(children=[
                    html.H6("Select your report to download"),
                    html.Div([dcc.Dropdown(id='reports',
                                           placeholder="Select your report...",
                                           options=[{'label': i, 'value': i} for i in
                                                    os.listdir("assets/profile_reports")],
                                           style={"background-color": "#CAECD8", "width": "100%"},
                                           multi=False,
                                           persistence=True,
                                           persistence_type='session'),
                              ], style={"background-color": "white", "width": "100%"}),
                    html.Br(),
                    dbc.Button(children=[html.I(className="fa-cloud-download"), "Download Report"],
                               id="download_html_pandas_report",
                               #className="mt-1"
                               ),
                    dcc.Download(id="download-report"),
                ]),
                dbc.Col(),
            ]),
            html.Br(),
            html.Br(),
            html.H6("Make sure to download your models or reports before continuing to"
                    " Section 'What's next', because all your progress will be lost."),
        ]
            # TODO: use modal to output congratulations section
        )
