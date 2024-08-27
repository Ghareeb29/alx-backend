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
