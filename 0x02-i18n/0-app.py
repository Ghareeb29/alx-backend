#!/usr/bin/env python3
"""
A simple Flask web application.
This module sets up a basic Flask app with a single route
that renders an index.html template.
"""

from flask import Flask, render_template
from typing import Any

app = Flask(__name__)


@app.route("/")
def index() -> Any:
    """
    Render the index page.

    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
