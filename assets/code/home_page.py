from dash import html

home_page = html.Div([html.Div([
            html.Img(src="assets/logo.png"),
            html.H1("NO DATA SCIENCE APP"),
            html.P("Welcome to the 'No data science app', where anything is possible"),
        ],
            style={
                'textAlign': 'center',
                "background-color": "white",
                "border-color": "white",
                "border-style": "solid"
            }
        ),
            html.Br(),
            html.Br(),
            html.Div(
                [html.P(children=[html.H4("What can I do within this application?", style={'textAlign': 'center'}),
                                  html.Hr(),
                                  html.P(["This app was designed for people that are not familiar with coding"
                                          " or are not in general familiar with the concepts of Data Science and"
                                          " Machine Learning or for data scientists that want a quick and 'dirty'"
                                          " solution."
                                          " With the help of this app, a person will be able to do the following"
                                          " things by only clicking a few buttons:"],
                                         style={"margin-left": "1em", "margin-bottom": "0px"}),
                                  html.Br(),
                                  html.Li(children=["Upload you dataset or choose one from the preloaded ones and"
                                                    " create some basic interactive visualizations."],
                                          style={"margin-left": "1em"}),
                                  html.Li(children=["Perform exploratory data analysis and download the report"
                                                    " at the end if you like it."], style={"margin-left": "1em"}),
                                  html.Li(children=["Train a variety of ML models. The objective can either be"
                                                    " specified as regression (predicting a continuous output,"
                                                    " i.e. final "
                                                    # " a class of objects whose class label is unknown using this"
                                                    # " model)"
                                                    ],
                                          style={"list-style-position": "outside", "margin-left": "1em"}),
                                  html.P("housing price) or as classification (predicting a class of objects whose "
                                         "class label is unknown using this model)",
                                         style={"margin-left": "2.5em", "margin-bottom": "0px"}),
                                  html.Li(children=["Download your best model and the EDA report."],
                                          style={"margin-left": "1em"}),
                                  html.Li(children=["Of course in the last page you can explore also other"
                                                    " options."], style={"margin-left": "1em"})
                                  ],
                        style={"border": "2px black solid", 'width': '100%'}),
                 ], style={"margin-left": "8%", "margin-right": "8%"}),
        ])
