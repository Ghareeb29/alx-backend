#!/usr/bin/env python3
"""
Flask app with internationalization support and mock user authentication.

This module sets up a Flask web application with support for multiple languages
using Flask-Babel, and implements a mock user authentication system.
It demonstrates how to handle language selection
based on URL parameters and user preferences,
as well as how to manage user sessions in a simple way.
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

    This function checks for a 'locale' parameter in the URL and returns it
    if it's a supported language. If not found or not supported, it falls back
    to the best match based on the Accept-Language header.

    Returns:
        str: The selected locale string.
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


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
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
