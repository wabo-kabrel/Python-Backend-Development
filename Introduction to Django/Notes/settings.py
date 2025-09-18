#1 What is settings.py?
# - settings.py is like the "control center" of your Django project.
# - It tells Django how your project should behave — from what database to use,
#   to how to load templates, serve static files, and keep things secure.
# - Think of it as your project's configuration file.
# - It is automatically created when you run `django-admin startproject myproject`.


#2. Location of settings.py
# - Inside your project folder:
#       myproject/
#       │
#       ├── manage.py
#       ├── myproject/
#       │   ├── __init__.py
#       │   ├── settings.py  ← 📍 this file
#       │   ├── urls.py
#   │   └── wsgi.py


#3. Key Settings You Must Understand
#i. INSTALLED_APPS
'''
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    ...
    'pages',  # ← your custom app
]
'''
    # - Purpose: Tells Django which apps to include in the project.
    # - Built-in apps (like admin, auth, etc.)
    # - Your own apps (like pages, blog, etc.)
    # - Third-party apps (like rest_framework, crispy_forms, etc.)

#ii. TEMPLATES
'''
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ← global templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                ...
            ],
        },
    },
]
'''
    # - Purpose: Controls how Django loads HTML templates.
    # - DIRS: Tells Django where to look for templates globally.
    # - APP_DIRS: Allows Django to look for templates/ folders 
    #   inside apps (like pages/templates/pages/home.html).

#iii. DATABASES
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # default: SQLite
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''
    # - Purpose: Configures the database your project uses.
    # - SQLite (default): good for development.
    # - PostgreSQL or MySQL: better for production.
    # - ENGINE: Specifies the database backend.
    # - NAME: The name of your database file or database.
    # - You’ll later change 'ENGINE' to 'django.db.backends.postgresql' when
    #   you set up PostgreSQL.

#iv. STATIC_URL and Static Files
'''
STATIC_URL = '/static/'
'''
    # - Purpose: Tells Django where to find CSS, JavaScript, and image files
    #   used by your frontend.
    # - You'll usually also add:
        # STATICFILES_DIRS = [BASE_DIR / 'static']  # where your custom static files live
    # - Example:
    #   <link rel="stylesheet" href="{% static 'css/styles.css' %}">

#v. MEDIA_URL and Uploaded Files
'''
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
'''
    # - Purpose:  Handles user-uploaded files (e.g., profile pictures, PDFs, etc.)
    # - Example:
        # - User uploads a profile photo → it’s saved in /media/photos/kabrel.jpg
        # - You serve it using MEDIA_URL

#vi. Example settings.py Overview (Simplified)
'''
# myproject/settings.py

DEBUG = True
SECRET_KEY = 'xyz123secretkey'
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    ...
    'pages',  # Your app
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
        ...
    }
]
'''

#4. Environment-Specific Settings (Dev vs Production)
# - Dev = debugging & experimenting
# - Prod = secure, stable, safe
# - Here's how to separate them:
#  Structure:
'''
myproject/
│
├── settings/
│   ├── __init__.py
│   ├── base.py
│   ├── development.py
│   └── production.py
'''
    # - base.py: shared settings
    # - development.py: DEBUG=True, use SQLite
    # - production.py: DEBUG=False, use PostgreSQL, add security
# - Then in manage.py or wsgi.py, set:
''' os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings.development")
'''


#5. Safely Managing Secret Keys and Debug Mode
# ❌ Avoid doing this in production:
'''
SECRET_KEY = 'hardcoded-secret-key'
DEBUG = True
'''
# ✅ Instead, use environment variables:
    # - Install python-decouple:
'''     pip install python-decouple
'''
    # - Create a .env file:
'''
        SECRET_KEY=your-secret
        DEBUG=True
'''
    # - Update settings.py:
'''
        from decouple import config

        SECRET_KEY = config('SECRET_KEY')
        DEBUG = config('DEBUG', default=False, cast=bool)
'''
    # - Now your secret key isn’t visible in the code!


#6.  Best Practices with settings.py
# - Use .env files:	                        Keep secrets secure
# - Turn DEBUG off in production:	        Avoid leaking sensitive info
# - Separate settings by environment:	    Better organization and safety
# - Use BASE_DIR:	                        Consistent path references
# - Keep INSTALLED_APPS clean:	            Only include what's used
