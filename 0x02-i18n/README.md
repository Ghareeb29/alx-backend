# 0x02-i18n

## Simple Flask Web Application

This project is a basic Flask web application that displays a "Hello world" message.

### Files

- `0-app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the index page.

### Requirements

- Python 3.7
- Flask

### Running the application

To run the application, use the following command:

```bash
python3 0-app.py
```

The application will be accessible at `http://localhost:5000`.

---

### Flask Babel Setup

This project demonstrates how to set up and configure Flask-Babel for internationalization in a Flask application.

### Setup

1. Install the required packages:

   ```bash
   pip3 install Flask==2.0.1 flask_babel==2.0.0
   ```

2. The main application file is `0-app.py`.

### Features

- Basic Flask application with a single route ('/')
- Flask-Babel integration for internationalization
- Configuration class (`Config`) to set language and timezone preferences

### Configuration

- Available languages: English (en) and French (fr)
- Default language: English
- Default timezone: UTC

### Running the Application

Execute the following command:

```bash
python3 0-app.py
```

The application will be accessible at `http://localhost:5000`.

### Code Structure

- `Config` class: Holds configuration for languages and Babel settings
- `babel`: Module-level variable instantiating Babel
- Flask app configuration using `app.config.from_object(Config)`

### Next Steps

- Implement language selection logic
- Add translations for supported languages
- Create language-specific templates

---

## Flask-Babel Locale Selector

This project demonstrates how to implement a locale selector in a Flask application using Flask-Babel.

### Files

- `2-app.py`: Main Flask application with Babel configuration and locale selector.
- `templates/2-index.html`: HTML template for the index page.

### Features

- Flask-Babel integration for internationalization.
- Automatic locale detection based on client's language preferences.
- Supports English (en) and French (fr) languages.

### Setup

1. Install required packages:

   ```bash
   pip3 install Flask==2.0.1 flask_babel==2.0.0
   ```

2. Run the application:

   ```bash
   python3 2-app.py
   ```

### Key Components

- `Config` class: Defines supported languages and Babel settings.
- `get_locale()` function: Selects the best matching language using `request.accept_languages`.
- `@babel.localeselector` decorator: Registers the `get_locale()` function with Flask-Babel.

### Usage

The application automatically selects the best matching language based on the client's `Accept-Language` header. No user interaction is required for language selection.

### Next Steps

- Implement language-specific translations.
- Add visual indicators for the selected language.
- Create routes to manually switch languages.

### Repository Information

- GitHub repository: `alx-backend`
- Directory: `0x02-i18n`
- Files: `2-app.py`, `templates/2-index.html`

---

## Flask-Babel Internationalization (i18n)

This project demonstrates how to implement internationalization in a Flask application using Flask-Babel.

### Files

- `3-app.py`: Main Flask application with Babel configuration and i18n support.
- `babel.cfg`: Babel configuration file for extraction.
- `templates/3-index.html`: HTML template with translatable strings.
- `translations/en/LC_MESSAGES/messages.po`: English translations.
- `translations/fr/LC_MESSAGES/messages.po`: French translations.
- `translations/en/LC_MESSAGES/messages.mo`: Compiled English translations.
- `translations/fr/LC_MESSAGES/messages.mo`: Compiled French translations.

### Setup and Usage

1. Install required packages:

   ```bash
   pip install Flask flask-babel
   ```

2. Run the extraction command:

   ```bash
   pybabel extract -F babel.cfg -o messages.pot .
   ```

3. Initialize translations:

   ```bash
   pybabel init -i messages.pot -d translations -l en
   pybabel init -i messages.pot -d translations -l fr
   ```

4. Edit the `.po` files in `translations/[en|fr]/LC_MESSAGES/` to provide translations.

5. Compile translations:

   ```bash
   pybabel compile -d translations
   ```

6. Run the application:

   ```bash
   python3 3-app.py
   ```

The application will display messages in English or French based on the user's browser language settings.

## Repository Information

- GitHub repository: `alx-backend`
- Directory: `0x02-i18n`
- Files: `3-app.py`, `babel.cfg`, `templates/3-index.html`, `translations/en/LC_MESSAGES/messages.po`, `translations/fr/LC_MESSAGES/messages.po`, `translations/en/LC_MESSAGES/messages.mo`, `translations/fr/LC_MESSAGES/messages.mo`

---

## Flask Internationalization (i18n) Task

### Overview

This project demonstrates how to implement internationalization in a Flask application using Flask-Babel. It includes functionality to force a particular locale by passing a `locale` parameter in the URL.

### Files

- `4-app.py`: Main Flask application file
- `templates/4-index.html`: HTML template for the index page
- `babel.cfg`: Babel configuration file
- `translations/`: Directory containing translation files

### Setup and Running

1. Ensure you have Python 3.7+ installed.
2. Install required packages:

   ```
   pip install Flask==3.0.0 Flask-Babel==4.0.0
   ```

3. Set up translations:

   ```
   pybabel extract -F babel.cfg -o messages.pot .
   pybabel init -i messages.pot -d translations -l en
   pybabel init -i messages.pot -d translations -l fr
   ```

4. Edit the `.po` files in `translations/en/LC_MESSAGES/messages.po` and `translations/fr/LC_MESSAGES/messages.po` to add your translations.
5. Compile translations:

   ```
   pybabel compile -d translations
   ```

6. Run the application:

   ```
   python3 4-app.py
   ```

### Usage

- Access the application at `http://127.0.0.1:5000`
- To force a specific locale, use the `locale` parameter in the URL:
  - English: `http://127.0.0.1:5000?locale=en`
  - French: `http://127.0.0.1:5000?locale=fr`

### Requirements

- All files interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- Code follows pycodestyle style (version 2.5)
- All Python files are executable
- All modules, classes, and functions have documentation

### Note

This project uses Flask 3.0 and Flask-Babel 4.0. Ensure compatibility when making changes or updates.
