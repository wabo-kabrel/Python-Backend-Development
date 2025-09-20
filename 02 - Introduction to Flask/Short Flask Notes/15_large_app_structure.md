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
Here's where the magic happens.

### 1. Application Factory (app/__init__.py)
Instead of creating the app globally, use a function `create_app()`.

**Why?**
- Let's you configure app dynamically.
- Useful for **testing** (e.g., test DB vs production DB).
- Allows multiple app instances.
```python
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
```

### 2. Blueprints (app/main/)
Blueprints let you organize features separately.
Instead of defining routes on the app directly, you define them on a blueprint.
- `__init__.py`
```python
from flask import Blueprint
main = Blueprint('main', __name__)
from . import views, errors
````

- `views.py`
```python
from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # save user, send email, etc.
        return redirect(url_for('.index'))  # notice the dot!
    return render_template('index.html',
                           form=form,
                           name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())
```

- `errors.py`
```python
from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
```

**👉 Key ideas:**
- Blueprints avoid circular imports.
- They're modular — you can have `auth`, `api`, `main` as separate blueprints.
- Routes inside blueprints are namespaced (`main.index` instead of `index`).
```

## 🚦 Launch Script `(manage.py)`
This is you app's entry point.
```python
#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
```

**👉 What it does:**
- Starts the app (`python manage.py runserver`).
- Manages migrations (`python manage.py db upgrade`).
- Runs tests (`python manage.py test`).
- Starts a Python shell with app preloaded (`python manage.py shell`).


## 📦 Dependencies (`requirements.txt`)
Keep track of versions so your app works the same everywhere.
```txt
Flask==0.10.1
Flask-Bootstrap==3.0.3.1
Flask-Mail==0.9.0
Flask-Migrate==1.1.0
Flask-Moment==0.2.0
Flask-SQLAlchemy==1.0
Flask-Script==0.6.6
Flask-WTF==0.9.4
```
**Generate it**
```bash
pip freeze > requirements.txt
```
**Install it:**
```bash
pip install -r requirements.txt
```

## 🧪 Unit Tests (`tests/`)
**Example:**
```python
import unittest
from flask import current_app
from app import create_app, db

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
```
**👉 Tests are run using:**
```bash
python manage.py test
```


## 🗄️ Database Setup
- Each config (dev, test, prod) has its own DB.
- Use **Flask-Migrate** for migrations.
- Run:

```bash
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```

## ✅ Recap (Big Picture)
1. **Split app into packages** → `app/`, `tests/`, `migrations/`.
2. **Configs** → `config.py` with different environments.
3. **App factory** → `create_app()` in `app/__init__.py`.
4. **Blueprints** → modular organization (`main/`, `auth/`, etc.).
5. **manage.py** → run, migrate, test, shell.
6. **requirements.txt** → track dependencies.
Unit tests → reliable, automated testing.

This structure makes your app:
✔ Scalable
✔ Testable
✔ Configurable
✔ Maintainable