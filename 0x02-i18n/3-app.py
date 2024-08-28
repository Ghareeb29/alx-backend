#!/usr/bin/env python3
"""
A Flask web application with Babel support and translations.
This module sets up a Flask app with internationalization features,
including automatic locale detection and message translations.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _
from typing import Any, Union

class Config:
    """Configuration class for Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale() -> Union[str, None]:
    """
    Determine the best match for supported languages.
    
    Returns:
        str: Best matching language code.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> Any:
    """
    Render the index page with translated content.
    
    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(debug=True)
