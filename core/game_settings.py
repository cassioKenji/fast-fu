import os

from werkzeug.datastructures import ImmutableDict

main_dir = os.path.split(os.path.abspath(__file__))[0]

screen_settings = ImmutableDict(
    {
        "WINDOW_TITLE": "My Python Game",
        "SCREEN_RES": (512, 288),
    }
)
