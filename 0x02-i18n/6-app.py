#!/usr/bin/env python3
"""
Flask app with internationalization support, mock user authentication,
and prioritized locale selection.

This module sets up a Flask web application with support for multiple languages
using Flask-Babel, implements a mock user authentication system, and provides
a prioritized method for selecting the appropriate locale.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration class for Flask app.

    This class defines configuration variables for the Flask application,
    including supported languages and default locale and timezone settings.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Retrieve a user based on a URL parameter.

    This function checks for a 'login_as' parameter in the URL and returns
    the corresponding user dictionary if found. If the user doesn't exist
    or the parameter is not provided, it returns None.

    Returns:
        Union[Dict, None]: A dictionary containing user information if found,
                           None otherwise.
    """
    login_id = request.args.get("login_as")
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """
    Execute before all other functions.

    This function runs before each request and sets the user (if any)
    as a global variable on flask.g.user.
    """
    g.user = get_user()


def get_locale() -> str:
    """
    Determine the best match for supported languages.

    This function implements a priority order for language selection:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale

    Returns:
        str: The selected locale string.
    """
    # 1. Locale from URL parameters
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    # 2. Locale from user settings
    if g.user and g.user["locale"] in app.config["LANGUAGES"]:
        return g.user["locale"]

    # 3. Locale from request header
    locale = request.accept_languages.best_match(app.config["LANGUAGES"])
    if locale:
        return locale

    # 4. Default locale
    return app.config["BABEL_DEFAULT_LOCALE"]


babel.init_app(app, locale_selector=get_locale)


@app.route("/", strict_slashes=False)
def index() -> str:
    """
    Render the index page.

    This function handles requests to the root URL
    and renders the index template.

    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(debug=True)
