import dash
from dash import html, callback, Output, Input, ALL, ctx
import dash_bootstrap_components as dbc

from utils.utils import filter_registry
from utils.card_grid import make_card_grid


def layout(code=None, **other):
    """
    Displays the apps in a card grid.
    May pass query stings to filter the examples.
    If using query strings, the variable name must be `code`.  eg `http://127.0.0.1:8050/?code=dropdown`
    """
    home_layout = html.Div(
        [
            dbc.Row(dbc.Col(html.Div(id="home-search-x-grid"))),
        ],
        className="p-4 mx-2",
    )
    return home_layout


@callback(
    Output("home-search-x-grid", "children"),
    Input("home", "n_clicks"),
)
def update(overview):
    input_id = ctx.triggered_id
    registry = dash.page_registry.values()

    # if input_id == "home":
    #     return make_card_grid(registry=registry)

    return make_card_grid(registry=registry)


dash.register_page(
    __name__,
    name="Home - Overview",
    title="Dash Example Index",
    description="This is the home page",
    path="/",
    layout=layout(),
)
