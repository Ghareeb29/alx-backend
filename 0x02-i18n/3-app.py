#!/usr/bin/env python3
"""
A Flask web application with Babel support and internationalization.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import Any, Union


class Config:
    """Configuration class for Flask app."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale() -> Union[str, None]:
    """Determine the best match for supported languages."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index() -> Any:
    """Render the index page."""
    return render_template(
        "3-index.html",
        home_title=_("Welcome to Holberton"),
        home_header=_("Hello world!"),
    )


if __name__ == "__main__":
    app.run(debug=True)
