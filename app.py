import os
from glob import glob
from joblib import dump
from pandas_profiling import ProfileReport
from pycaret.regression import setup as setup_regr
from pycaret.regression import compare_models as compare_models_reg
from pycaret.regression import pull as pull_regr
from pycaret.classification import setup as setup_class
from pycaret.classification import compare_models as compare_models_class
from pycaret.classification import pull as pull_class

import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table

import pandas as pd
import plotly.express as px

from assets.code.sidebar import sidebar
from assets.code.config import CONTENT_STYLE

from assets.code.home_page import home_page
from assets.code.upload_page import (upload_page, return_output_data,
                                     parse_contents, parse_contents_df)
from assets.code.eda_page import eda_page
from assets.code.modelling_page import modelling_page
from assets.code.download_page import download_page
from assets.code.whatsnext_page import whatsnext_page

# FONT_AWESOME = (
#     "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
# )
FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css"
)

# external_stylesheets = [dbc.themes.BOOTSTRAP, FONT_AWESOME]

external_style = ["assets/fontawesome.css"]
external_stylesheets = [dbc.themes.BOOTSTRAP, external_style]

app = dash.Dash(external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True,
                title="No Data Science App",
                meta_tags=[{"charset": "utf-8"},
                           {"name": "viewport",
                            "content": "width=device-width"}])


content = html.Div(id="page-content", style=CONTENT_STYLE)
data_store = dcc.Store(id='stored-data', storage_type="local")
filename_store = dcc.Store(id='stored-filename', storage_type="local")

app.layout = html.Div([dcc.Location(id="url"),
                       sidebar,
                       content,
                       data_store,
                       filename_store
                       ])


# ------- CALLBACKS SECTION -------
# ---------------------------------


# ------- HOME PAGE CALLBACKS -------
# -----------------------------------


@app.callback(Output("page-content", "children"),
              Input("url", "pathname"))
def render_page_content(pathname):

    if pathname == "/":

        return home_page

    elif pathname == "/upload_page":

        return upload_page

    elif pathname == "/eda_page":

        return eda_page

    elif pathname == "/modelling_page":

        return modelling_page

    elif pathname == "/download_page":

        return download_page

    elif pathname == "/whatsnext_page":

        return whatsnext_page

    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


@app.callback(Output("modal", "is_open"),
              Input("open", "n_clicks"),
              Input("close", "n_clicks"),
              State("modal", "is_open"))
def toggle_modal(n1, n2, is_open):

    if n1 or n2:
        return not is_open
    return is_open


# ------- UPLOAD PAGE CALLBACKS -------
# -------------------------------------

@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              Input("preloaded_dataset", "value"),
              State('upload-data', 'filename'))
def update_output(list_of_contents, preloaded, list_of_names):
    # used to detect which of the two inputs triggered the output
    # button or preloaded datasets
    user_click = dash.callback_context.triggered[0]['prop_id'].split('.')[0]

    # provides current values of the states when the callback was triggered
    # callback_states = dash.callback_context.states.values()
    # callback_inputs = dash.callback_context.inputs.values()  # is the equivalent for inputs

    if user_click == "upload-data":

        if list_of_contents:  # is not None:
            children = [
                parse_contents(c, n) for c, n in
                zip(list_of_contents, list_of_names)]
            return children
    else:
        if preloaded:  # is not None:
            df = pd.read_csv(f"assets/datasets/{preloaded}")
            return return_output_data(df, preloaded)


@app.callback(Output('stored-data', 'data'),
              Input('upload-data', 'contents'),
              Input("preloaded_dataset", "value"),
              State('upload-data', 'filename'))
def update_output_data_stored(list_of_contents, preloaded, list_of_names):

    user_click = dash.callback_context.triggered[0]['prop_id'].split('.')[0]

    if user_click == "upload-data":

        if list_of_contents is not None:
            children = [
                parse_contents_df(c, n) for c, n in
                zip(list_of_contents, list_of_names)]

            df = pd.DataFrame.from_records(children[0]).to_dict('records')
            return df
    else:
        if preloaded is not None:
            df = pd.read_csv(f"assets/datasets/{preloaded}").to_dict('records')
            return df


@app.callback(Output('stored-filename', 'data'),
              Input('upload-data', 'contents'),
              Input("preloaded_dataset", "value"),
              State('upload-data', 'filename'))
def update_output_filename_stored(list_of_contents, preloaded, list_of_names):

    user_click = dash.callback_context.triggered[0]['prop_id'].split('.')[0]

    if user_click == "upload-data":
        if list_of_contents is not None:
            return list_of_names
    else:
        if preloaded is not None:
            return preloaded


@app.callback(Output('output-div', 'children'),
              Input('submit-button', 'n_clicks'),
              Input('plot_type', 'value'),
              Input('xaxis-data', 'value'),
              Input('yaxis-data', 'value'),
              State('stored-data', 'data'), )
def make_graphs(n, plot, x_data, y_data, data):

    if n is None:
        return dash.no_update
    else:
        if plot == "  Bar Plot":
            bar_fig = px.bar(data, x=x_data, y=y_data)
            return dcc.Graph(figure=bar_fig)
        elif plot == "  Scatter Plot":
            scatter_fig = px.scatter(data, x=x_data, y=y_data)
            return dcc.Graph(figure=scatter_fig)
        else:
            hist_fig = px.histogram(data, x=x_data)
            return dcc.Graph(figure=hist_fig)


# ------- EDA PAGE CALLBACKS -------
# ----------------------------------


@app.callback(Output('automatic_eda', 'children'),
              Input('second_step_eda', 'n_clicks'),
              State('stored-data', 'data'),
              State('stored-filename', 'data'))
def update_output_eda(button_click, data, filename):
    if button_click is None:
        return dash.no_update
    else:
        data = pd.DataFrame.from_records(data)
        df = data.copy()

        if "Unnamed: 0" in df.columns:
            df = df.drop(["Unnamed: 0"], axis=1)

        # run pandas profiling and save to assets folder, then read it from there and display it
        profile = ProfileReport(df, title="Pandas Profiling Report")
        profile.to_file(
            f"assets/profile_reports/profile_report_{filename.split('.csv')[0]}_{str(int(button_click))}.html")

        children = html.Iframe(
            src=f"assets/profile_reports/profile_report_{filename.split('.csv')[0]}_{str(int(button_click))}.html",
            style={"height": "1080px", "width": "100%"})

        return children


# ------- MODELLING PAGE CALLBACKS -------
# ----------------------------------------


@app.callback(Output('target', 'options'),
              Input('choose_target', 'n_clicks'),
              State('stored-data', 'data'))
def update_model_options(n_clicks, data):
    if n_clicks:
        data = pd.DataFrame.from_records(data)
        df = data.copy()
        lst = [{'label': i, 'value': i} for i in df.columns]
        return lst
    else:
        return []


@app.callback(Output('automatic_modelling', 'children'),
              Input('third_step_modelling', 'n_clicks'),
              State('ml_type', 'value'),
              State('target', 'value'),
              State('stored-data', 'data'),
              State('stored-filename', 'data'))
def update_output_modelling(button_click, ml_type, target_column, data, filename):
    if button_click:
        data = pd.DataFrame.from_records(data)
        df = data.copy()

        # Generate random characters for filenames if needed
        # def random_char(y):
        #     return ''.join(random.choice(string.ascii_letters) for x in range(y))

        if "Unnamed: 0" in df.columns:
            df = df.drop(["Unnamed: 0"], axis=1)

        if ml_type == "classification":
            s = setup_class(data=df,
                            target=target_column,
                            silent=True,
                            session_id=123,
                            verbose=False)
            best_model = compare_models_class(verbose=False)
            table_results = pull_class()
            table_results = table_results.round(3)
            # save_model(model=best_model, model_name="assets/best_model")
            model_name = str(int(button_click)) + ")" + filename.split(".csv")[0] + "_" + "_classification_model"
            dump(best_model, f'assets/models/{model_name}.joblib')
        else:
            s = setup_regr(data=df,
                           target=target_column,
                           silent=True,
                           session_id=123,
                           verbose=False)
            best_model = compare_models_reg(verbose=False)
            table_results = pull_regr()
            table_results = table_results.round(3)
            # save_model(model=best_model, model_name="assets/best_model")
            model_name = str(int(button_click)) + ")" + filename.split(".csv")[0] + "_" + "_regression_model"
            dump(best_model, f'assets/models/{model_name}.joblib')

        return html.Div([

            dash_table.DataTable(
                data=table_results.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in table_results.columns],
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
            html.Hr(),
        ])


# ------- DOWNLOAD PAGE CALLBACKS -------
# ---------------------------------------
@app.callback(Output('models', 'options'),
              Input('refreshdownload', 'n_clicks')
              )
def update_download_models(n_clicks):
    if n_clicks:
        model_names = [{'label': i, 'value': i} for i in os.listdir("assets/models")]
        return model_names
    else:
        return []


@app.callback(Output('reports', 'options'),
              Input('refreshdownload', 'n_clicks')
              )
def update_download_reports(n_clicks):
    if n_clicks:
        report_names = [{'label': i, 'value': i} for i in os.listdir("assets/profile_reports")]
        return report_names
    else:
        return []


@app.callback(Output('download-model', 'data'),
              Input('fourth_step_model_download', 'n_clicks'),
              State('models', 'value'))
def download_model(n_clicks, model_name):
    if n_clicks:
        return dcc.send_file(f"assets/models/{model_name}")


@app.callback(Output('download-report', 'data'),
              Input("download_html_pandas_report", 'n_clicks'),
              State('reports', 'value'))
def download_eda_report(button_click, report_name):
    if button_click is None:
        return dash.no_update
    else:
        return dcc.send_file(f"assets/profile_reports/{report_name}")


# ------- WHATSNEXT PAGE CALLBACKS -------
# ----------------------------------------

@app.callback(Output('delete_model_if_exists', 'data'),
              Input('whatisnext', 'n_clicks'))
def delete_model(n_clicks):
    if n_clicks:
        try:
            if os.path.exists("assets/models"):
                entries = os.listdir("assets/models")
                for entry in entries:
                    os.remove(f"assets/models/{entry}")
        except:
            pass


@app.callback(Output('delete_pandas_profilling_if_exists', 'data'),
              Input('whatisnext', 'n_clicks'))
def delete_eda_report(n_clicks):
    if n_clicks:
        try:
            if os.path.exists("assets/profile_reports"):
                entries = os.listdir("assets/profile_reports")
                for entry in entries:
                    os.remove(f"assets/profile_reports/{entry}")
        except:
            pass


if __name__ == "__main__":
    app.run_server(debug=False)
