# 0x02-i18n

## Task 0

### Simple Flask Web Application

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

## Task 1

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

## Task 2

### Flask-Babel Locale Selector

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

   ```
   pip3 install Flask==2.0.1 flask_babel==2.0.0
   ```

2. Run the application:

   ```
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
