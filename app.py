import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from whitenoise import WhiteNoise
from utils.utils import project_apps
from quart import Quart, websocket
import threading


app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root="assets/")
# server = Quart(__name__)
# server.asgi_app = WhiteNoise(server.asgi_app, root="assets/")

for k in project_apps:
    new_callback_map = project_apps[k].callback_map
    new_callback_list = project_apps[k]._callback_list

    app.callback_map.update(new_callback_map)
    app._callback_list.extend(new_callback_list)

navbar = dbc.NavbarSimple(
    [
        dbc.Button("Overview", id="home", href=dash.get_relative_path("/"), color="secondary", size="sm", className="m-1",),
        dbc.Button(
            "Google",
            id="google",
            href="https://google.com",
            target="_blank",
            color="secondary",
            size="sm",
            className="m-1 ",
        ),
    ],
    brand="Project Demos Page",
    # brand_href=dash.get_relative_path("/"),
    color="primary",
    dark=True,
    fixed="top",
    className="mb-2 fs-3 ",
)

footer = html.H5(
    [
        dcc.Link(
            "External Link To Google",
            className="bi bi-github",
            href="https://google.com",
            target="_blank",
        )
    ],
    className="p-4 mt-5 text-center",
)

app.layout = html.Div(
    [
        navbar,
        dbc.Container(dash.page_container, fluid=True, style={"marginTop": "4rem"}),
        footer,
        dcc.Location(id="url", refresh=True),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)

