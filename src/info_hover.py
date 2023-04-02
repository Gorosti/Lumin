import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash import html


def create_title_with_info_hover(title: str, info_text_dict):
    return dmc.Grid(
        children=[
            dmc.Col(
                html.Div(title),
                span="content",
            ),
            dmc.Col(
                dbc.Button(
                    id=f"tooltip-target_{title.strip()}",
                    className="bi bi-info-circle",
                    color='white',
                    style={'float': 'right', 'margin': 'auto'},
                ),
                span="content",
            ),
            dbc.Tooltip(
                info_text_dict[title],
                target=f"tooltip-target_{title.strip()}",
                autohide=False,
            ),
        ],
        align="center",
    )


info_texts = {
    'Select Data': 'Select an excel file from your local computer to do the analysis on. This excel should ' +
                   'contain different sheets for each sample',
    'Fitted Profiles': 'Here the fit of each profile is shown',
    'Initial Guess': 'The fitting algorithm needs an initial guess to strat from. Make sure this guess is reasonably' +
                     'close the data to make sure the fitting is robust',
    'ERC Graph': 'If the age for two or more samples is known the estimated age for the other samples is displayed' +
                 'in this figure',
}
