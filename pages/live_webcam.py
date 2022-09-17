import dash

from utils.display import project_app


dash.register_page(
    __name__,
    description="Live Webcam"
)

filename = __name__.split("pages.")[1]


notes = """
#### Components in App:
- TBA
#### Documentation:  
- TBA
#### Created by:
- TBA
"""


layout = project_app(filename, notes=notes)
