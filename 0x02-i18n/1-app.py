#!/usr/bin/env python3
"""
A simple Flask web application with Babel support.
This module sets up a basic Flask app with a single route
that renders an index.html template, and configures Babel
for internationalization.
"""

from flask import Flask, render_template
from flask_babel import Babel
from typing import Any


class Config:
    """Configuration class for Flask app."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index() -> Any:
    """
    Render the index page.

    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
