# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "22rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

ml_types = ["classification", "regression"]

datasets = {"Iris.csv": "Iris",
            "California_Housing.csv": "California Housing",
            "heart_attack.csv": "Heart Attack",
            "Life_Expectancy_Data.csv": "Life Expectancy",
            "titanic_survival.csv": "Titanic Survival"}
