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

---

# Flask Internationalization (i18n) with Mock Authentication

## Overview

This project demonstrates the implementation of internationalization in a Flask application using Flask-Babel, along with a mock user authentication system. It showcases handling different languages and displaying personalized messages based on user login status.

## Project Structure

- `5-app.py`: Main Flask application file with mock authentication
- `templates/5-index.html`: HTML template for the index page
- `babel.cfg`: Babel configuration file
- `translations/`: Directory containing translation files
- `README.md`: This file, containing project documentation

## Features

- Internationalization support for English and French
- Mock user authentication system
- Dynamic content based on user login status

## Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- Flask 3.0
- Flask-Babel 4.0
- Pycodestyle 2.5

## Setup and Running

1. Ensure you have Python 3.7+ installed on Ubuntu 18.04 LTS.
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

6. Ensure all Python files are executable:

   ```
   chmod +x *.py
   ```

7. Run the application:

   ```
   ./5-app.py
   ```

## Usage

- Access the application at `http://127.0.0.1:5000`
- To simulate logging in as a user, use the `login_as` parameter in the URL:
  - e.g., `http://127.0.0.1:5000/?login_as=2` to log in as Beyonce
- To change the language, use the `locale` parameter:
  - e.g., `http://127.0.0.1:5000/?locale=fr` for French

## Mock Users

The application uses a predefined set of mock users:

- ID 1: Balou (French)
- ID 2: Beyonce (English)
- ID 3: Spock (Klingon)
- ID 4: Teletubby (No specific locale)

## Development Notes

- All Python files use the shebang `#!/usr/bin/env python3`
- Code follows pycodestyle style (version 2.5)
- All modules, classes, and functions have documentation
- All functions and coroutines are type-annotated

## Testing Documentation

To test the documentation of modules, classes, and functions, you can use the following commands:

- For modules: `python3 -c 'print(__import__("5-app").__doc__)'`
- For classes: `python3 -c 'print(__import__("5-app").Config.__doc__)'`
- For functions: `python3 -c 'print(__import__("5-app").get_user.__doc__)'`

Ensure all documentation consists of complete sentences explaining the purpose of the module, class, or method.

---

# Flask Internationalization (i18n) with Authentication and Locale Priority

## Overview

This project demonstrates an advanced implementation of internationalization in a Flask application using Flask-Babel. It features a mock user authentication system and a prioritized locale selection mechanism.

## Key Features

- Internationalization support for English and French
- Mock user authentication system
- Prioritized locale selection based on:
  1. URL parameters
  2. User preferences
  3. Request headers
  4. Default locale

## Files

- `6-app.py`: Main Flask application file
- `templates/6-index.html`: HTML template for the index page
- `babel.cfg`: Babel configuration file
- `translations/`: Directory containing translation files

## Setup and Running

1. Ensure you have Python 3.7+ installed on Ubuntu 18.04 LTS.
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

4. Edit the `.po` files in `translations/[en|fr]/LC_MESSAGES/messages.po` to add your translations.
5. Compile translations:

   ```
   pybabel compile -d translations
   ```

6. Run the application:

   ```
   python3 6-app.py
   ```

## Usage and Testing

- Access the base URL: `http://127.0.0.1:5000/`
- Test URL parameter: `http://127.0.0.1:5000/?locale=fr`
- Test user settings:
  - `http://127.0.0.1:5000/?login_as=1` (Balou, French)
  - `http://127.0.0.1:5000/?login_as=2` (Beyonce, English)
- Test with no specific locale: `http://127.0.0.1:5000/?login_as=4` (Teletubby)

## Mock Users

- ID 1: Balou (French)
- ID 2: Beyonce (English)
- ID 3: Spock (Klingon)
- ID 4: Teletubby (No specific locale)

## Development Notes

- Python version: 3.7
- Style guide: pycodestyle 2.5
- All functions and coroutines are type-annotated
- Comprehensive docstrings for all modules, classes, and functions

## Testing Documentation

To view documentation:

- Modules: `python3 -c 'print(__import__("6-app").__doc__)'`
- Classes: `python3 -c 'print(__import__("6-app").Config.__doc__)'`
- Functions: `python3 -c 'print(__import__("6-app").get_locale.__doc__)'`
