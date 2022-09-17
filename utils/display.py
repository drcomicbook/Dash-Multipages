from dash import dcc
import dash_bootstrap_components as dbc

from utils.utils import project_apps


def project_app(filename, run=True, notes=None):
    """
    Creates the "code and show layout for an example dash app.
    - `filename`:
       The path to the file with the sample app code.
    - `run`:
        bool (default: True) Whether to run the app
    - `notes`:
        str (default: None)  Notes or tutorial to display with the app.  Text may include markdown formatting
        as it will be displayed in a dcc.Markdown component
    """
    run_app = project_apps[filename].layout if run else ""
    return make_project_app(run_app, notes)


def make_project_app(show_app, notes):
    """
    This is the default layout for the "code and show"
    It displays the app and the code side-by-side on large screens, or
    the app first, followed by the code on smaller screens.
    It also has a dcc.Clipboard to copy the code.  Notes will display
    in a dcc.Markdown component below the app.
    """
    created_app = dbc.Row([
            dbc.Card(show_app, style={"padding": "10px"})
            if show_app
            else None,
            dcc.Markdown(notes, className="m-4", link_target="_blank")
            if notes
            else None,
        ],
        className="p-4",
    )

    return created_app
