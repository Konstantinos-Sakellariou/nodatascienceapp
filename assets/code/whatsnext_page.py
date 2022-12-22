from dash import html

whatsnext_page = html.Div(id="steps",
                          children=[html.Div([html.Div([
                              html.Img(src="assets/logo.png"),
                              html.H2("Critical ML Steps"),
                              html.Br(),
                              html.P(
                                  "Until this point you managed to create an exploratory report and download the best models"
                                  " according to your preferences, however, machine learning and data science are really broad"
                                  " fields and you can imagine that there are additional steps to be taken to ensure that"
                                  " the project you are working on will be succesful."),
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
                                  [html.P(children=[html.H4("Which are the critical steps?",
                                                            style={'textAlign': 'center'}),
                                                    html.Hr(),
                                                    html.P(
                                                        [
                                                            "In this section you can find all additional and essential steps"
                                                            " throughout the lifecycle of ML project. Below you can also find"
                                                            " a short description for each and every step. In any case you can"
                                                            " contact us (Contact page) and discuss all these possibilities for your"
                                                            " project."],
                                                        style={"margin-left": "1em", "margin-bottom": "0px"}),
                                                    html.Br(),
                                                    html.Li(
                                                        children=["Exploring and understand the metrics for regression"
                                                                  " and classification."],
                                                        style={"margin-left": "1em"}),
                                                    html.Li(children=["Customized metrics for business objective."],
                                                            style={"margin-left": "1em"}),
                                                    html.Li(children=[
                                                        "Identify and understand the most important features."],
                                                            style={"list-style-position": "outside",
                                                                   "margin-left": "1em"}),
                                                    html.Li(
                                                        children=["Hyperparameter Tuning"],
                                                        style={"margin-left": "1em"}),
                                                    html.Li(
                                                        children=["Interpretability of the model(s) and predictions."],
                                                        style={"margin-left": "1em"}),
                                                    html.Li(children=["Deploy and maintain model performance"],
                                                            style={"margin-left": "1em"}),
                                                    html.Li(children=[
                                                        "Understading the drifting concept and act accordingly."],
                                                        style={"margin-left": "1em"}),
                                                    html.Br(),
                                                    html.P(
                                                        ["Of course we must not forget that the most essential piece"
                                                         " of every project are the data. Quality of models depend"
                                                         " highly on quality of data. If the data are not quality"
                                                         " sufficient to"
                                                         " solve the problem, then even the best algorithms cannot"
                                                         " do much in order to perform higly enough."
                                                         " This is often referred as"
                                                         " the GIGO phenomenon, which stands for Garbage In Garbage"
                                                         " Out (referring to data of course)."],
                                                        style={"margin-left": "1em", "margin-bottom": "0px"}),
                                                    html.Br(),
                                                    ],
                                          style={"border": "2px black solid", 'width': '100%'}),
                                   ], style={"margin-left": "8%", "margin-right": "8%"}),
                          ]),
                              html.Br(),
                              html.Br(),
                              html.Br(),
                              html.H4("Exploring and understanding the metrics for regression"
                                      " and classification", style={'textAlign': 'center'}),
                              html.Hr(),
                              html.P(["Let's start with the most importannt difference between classification and "
                                      " regression problems. Fundamentally, classification is about predicting a category"
                                      " and regression is about predicting a continuous output. There are so many"
                                      " metrics that one can be confused, so understanding the research objective"
                                      " at the beginning is critical. If you deal with a classification problem"
                                      " first answer the type of classification (binary, multiclass or multilabel)"
                                      " and then choose your optimization metric. Popular classification metrics are:"
                                      " accuracy, precision, recall, area under the curve and the f1 score."
                                      " Typically for regression problems you have to look if there is any time"
                                      " relationship so you can formulate your problem as a time-series regession problem"
                                      " and make use of popular regression metrics like, root mean squared error,"
                                      " mean squared error, explained variance, mean absolute error.",
                                      html.Br(),
                                      html.Br(),
                                      html.P(children=["Find popular metrics: ",
                                                       html.A(children=[" Scikit-Learn"], target="_blank",
                                                              href="https://scikit-learn.org/stable/modules"
                                                                   "/model_evaluation.html")])],
                                     style={"margin-left": "1em", "margin-bottom": "0px"}),
                              html.Br(),
                              html.Br(),
                              html.H4("Customized metrics for specific business objective",
                                      style={'textAlign': 'center'}),
                              html.Hr(),
                              html.P(["Find the importance of tailored metrics for the specific project"
                                      " needs. Building an ML model is an amazing experience but evaluating its business"
                                      " value can be difficult depending on the machine learning metrics you are"
                                      " following. Is the AUC (Area Under the ROC curve) meaningful for your product"
                                      " owner or stakeholder? Developing machine learning software in a business context"
                                      " comes with new priorities. Most of the time, your model should respond to a"
                                      " user’s need. Therefore, you need to make sure you are bringing value to them."
                                      " How do I make sure I am building the right tool? Metrics!",
                                      html.Br(),
                                      html.Br(),
                                      html.P(children=["Read on this source: ",
                                                       html.A(children=[" Why tailored metrics are important?"],
                                                              target="_blank",
                                                              href="https://www.sicara.fr/blog-technique/machine-learning"
                                                                   "-metrics-essentials")])
                                      ],
                                     style={"margin-left": "1em", "margin-bottom": "0px"}),
                              html.Br(),
                              html.Br(),
                              html.H4("Identify and understand the most important features",
                                      style={'textAlign': 'center'}),
                              html.Hr(),
                              html.P(["Feature Importance refers to techniques that calculate a score for all the input"
                                      " features for a given model — the scores simply represent the 'importance' of each"
                                      " feature. In other words, feature (variable) importance indicates how much each"
                                      " feature contributes to"
                                      " the model prediction. Basically, it determines the degree of usefulness of a"
                                      " specific variable for a current model and prediction.",
                                      html.Br(),
                                      html.Br(),
                                      html.P(children=["Read on this sources: ",
                                                       html.A(children=[" Understanding Feature Importance"],
                                                              target="_blank",
                                                              href="https://towardsdatascience.com/understanding-feature-"
                                                                   "importance-and-how-to-implement-it-in-python-ff0287b20285"),
                                                       ", ",
                                                       html.A(children=[" What is Feature Importance"],
                                                              target="_blank",
                                                              href="https://www.baeldung.com/cs/ml-feature-importance")
                                                       ])
                                      ],
                                     style={"margin-left": "1em", "margin-bottom": "0px"}),
                              html.Br(),
                              html.Br(),
                              html.H4("Hyperparameter Tuning",
                                      style={'textAlign': 'center'}),
                              html.Hr(),
                              html.P(["Hyperparameter tuning consists of finding a set of optimal hyperparameter values"
                                      " for a learning algorithm while applying this optimized algorithm to any data set."
                                      " That combination of hyperparameters maximizes the model’s performance, minimizing"
                                      " a predefined loss function to produce better results with fewer errors. Note that"
                                      " the learning algorithm optimizes the loss based on the input data and tries to"
                                      " find an optimal solution within the given setting. However, hyperparameters"
                                      " describe this setting exactly.",
                                      html.Br(),
                                      html.Br(),
                                      html.P(children=["Read on this sources: ",
                                                       html.A(children=[" What is Hyperparameter Tuning"],
                                                              target="_blank",
                                                              href="https://www.anyscale.com/blog/what-is"
                                                                   "-hyperparameter-tuning"),
                                                       ", ",
                                                       html.A(children=[" Why Hyperparameter Tuning"],
                                                              target="_blank",
                                                              href="https://medium.com/analytics-vidhya/why-hyper"
                                                                   "-parameter-tuning-is-important-for"
                                                                   "-your-model-1ff4c8f145d3")
                                                       ])
                                      ],
                                     style={"margin-left": "1em", "margin-bottom": "0px"}),
                              html.Br(),
                              html.Br(),
                              html.H4("Model and prediction Interpetability",
                                      style={'textAlign': 'center'}),
                              html.Hr(),
                              html.P(["Interpretability is the degree to which a human can understand the cause of a"
                                      " decision. Or in other words: Interpretability is the degree to which a human can"
                                      " consistently predict the model’s result. The higher the interpretability of"
                                      " a machine learning model, the easier it is for someone to comprehend why certain"
                                      " decisions or predictions have been made. A model is better interpretable than"
                                      " another model if its decisions are easier for a human to comprehend than"
                                      " decisions from the other mode. We can achieve interpretability by calculating"
                                      " the SHAP values. SHAP values (SHapley Additive exPlanations) is a method based"
                                      " on cooperative game theory and used to increase transparency and"
                                      " interpretability of machine learning models.",
                                      html.Br(),
                                      html.Br(),
                                      html.P(children=["Read on this sources: ",
                                                       html.A(children=[" Interpretable Machine Learning"],
                                                              target="_blank",
                                                              href="https://christophm.github.io/interpretable-ml"
                                                                   "-book/interpretability.html"),
                                                       ", ",
                                                       html.A(children=[" SHAP values"],
                                                              target="_blank",
                                                              href="https://shap.readthedocs.io/en/latest/")
                                                       ])
                                      ],
                                     style={"margin-left": "1em", "margin-bottom": "0px"}),
                              html.Br(),
                              html.Br(),
                              html.H4("Deploy and maintain model performance",
                                      style={'textAlign': 'center'}),
                              html.Hr(),
                              html.P(["The goal of building a machine learning application is to solve a problem, and a"
                                      " ML model can only do this when it is actively being used in production. As such,"
                                      " ML model deployment is just as important as ML model development.Deployment is"
                                      " the process by which a ML model is moved from an offline environment and"
                                      " integrated into an existing production environment, such as a live application."
                                      " It is a critical step that must be completed in order for a model to serve its"
                                      " intended purpose and solve the challenges it is designed for. ",
                                      html.Br(),
                                      html.Br(),
                                      html.P(children=["Read on this sources: ",
                                                       html.A(children=[" What does it take?"],
                                                              target="_blank",
                                                              href="https://www.qwak.com/post/what-does-it-take-to"
                                                                   "-deploy-ml-models-in-production"),
                                                       ", ",
                                                       html.A(children=[" Model Deployment Challenges"],
                                                              target="_blank",
                                                              href="https://neptune.ai/blog/model-deployment"
                                                                   "-challenges-lessons-from-ml-engineers")
                                                       ])
                                      ],
                                     style={"margin-left": "1em", "margin-bottom": "0px"}),
                              html.Br(),
                              html.Br(),
                              html.H4("Understading the drifting concept and act accordingly.",
                                      style={'textAlign': 'center'}),
                              html.Hr(),
                              html.P(["In predictive analytics and machine learning, concept drift means that the"
                                      " statistical properties of the target variable, which the model is trying to"
                                      " predict, change over time in unforeseen ways. This causes problems because the"
                                      " predictions become less accurate as time passes.The term concept refers to the"
                                      " quantity to be predicted. More generally, it can also refer to other phenomena"
                                      " of interest besides the target concept, such as an input, but, in the context"
                                      " of concept drift, the term commonly refers to the target variable. Data drift is"
                                      " one of the top reasons model accuracy degrades over time. For machine learning"
                                      " models, data drift is the change in model input data that leads to model"
                                      " performance degradation. Monitoring data drift helps detect these model"
                                      " performance issues.",
                                      html.Br(),
                                      html.Br(),
                                      html.P(children=["Read on this sources: ",
                                                       html.A(children=[" How to break a model in 20 days"],
                                                              target="_blank",
                                                              href="https://www.evidentlyai.com/blog/tutorial-1-model"
                                                                   "-analytics-in-production"),
                                                       ", ",
                                                       html.A(children=[" Why data drift detection is important?"],
                                                              target="_blank",
                                                              href="https://towardsdatascience.com/why-data-drift"
                                                                   "-detection-is-important-and-how-do-you-automate"
                                                                   "-it-in-5-simple-steps-96d611095d93")
                                                       ])
                                      ],
                                     style={"margin-left": "1em", "margin-bottom": "0px"}),

                              html.Div(id="delete_model_if_exists"),
                              html.Div(id="delete_pandas_profilling_if_exists"),
                          ]
                          )
