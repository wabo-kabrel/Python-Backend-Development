# Why We Need Large Application Structure
- Small Flask apps often live in a single file (`hello.py`). That's fine for demos or small project.
- But when your app grows (user authentication, email support, APIs, database models, multiple features), keeping everything in one file becomes **unmanageable**.
- Flask doesn't force  a structure like Django does — **you must design one yourself**.

👉 The solution is:
- Break the app into **packages (folders)** and **modules(files)**.
- Use **factories** and **blueprints** so your app is flexible, testable, and scalable.


## 📂 Project Structure
```php
flasky/
│- app/                   # Main application package
│   │- templates/         # Jinja2 templates
│   │- static/            # CSS, JS, images
│   │- main/              # A blueprint
│   │   |- __init__.py
│   │   |- views.py
│   │   |- errors.py
│   │   |- forms.py
│   │- __init__.py        # app factory lives here
│   │- models.py          # database models
│   │- email.py           # email helper functions
│
│- migrations/            # database migration scripts (Flask-Migrate)
│- tests/                 # unit tests
│   │- test_basics.py
│   │- __init__.py
│
│- venv/                  # virtual environment
│- requirements.txt       # dependencies
│- config.py              # configuration settings
│- manage.py              # entry point to run app
```

### Top-Level Folders
1. **app/** → The actual Flask app (all code lives here).
2. **migrations/** → Auto-generated DB migration scripts.
3. **tests/** → Automated unit tests.
4. **venv/** → Your isolated Python environment.

### Key Files
- **requirements.txt** → "shopping list" of packages + versions.
- **config.py** → Central place for app configuration (debug, databases, mail, etc.).
- **manage.py** → Script to launch/manage the app (start, migrate, test, etc.).


## ⚙️ Configuration (`config.py`)
Different environments need different settings:
- Development → debugging on, local DB.
- Testing → test DB, special configs.
- Production → real DB, email, logging.

```python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass  # can add config-specific setup later

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

**👉 Key ideas:**
- Config inherits from a base called `Config`.
- Use **environment variables** for sensitive info (`MAIL_PASSWORD`, `SECRET_KEY`).
- App picks which config to use via an environment variable (`FLASK_CONFIG`)


## 🏗️ Application Package (app/)