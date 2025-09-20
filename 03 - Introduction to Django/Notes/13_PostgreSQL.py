#1. Why PostgreSQL over SQLite?
# - SQLite: Lightweight, file-based, suitable for small projects.
# - PostgreSQL: Robust, scalable, supports advanced features (e.g., concurrency, complex queries).
# - Choose PostgreSQL for production environments and larger applications.
# - In real-world Django projects, PostgreSQL is the standard.


#2. Installing PostgreSQL
# - On windows: Download from https://www.postgresql.org/download/


#3. Creating a Database and User
# - Switch to the PostgreSQL shell using the command: `sudo -u postgres psql`
# - Create a database using: `CREATE DATABASE myprojectdb;`
# - Create a user with password using: `CREATE USER myprojectuser WITH PASSWORD 'mypassword';`
# - Grant privileges using: `GRANT ALL PRIVILEGES ON DATABASE myprojectdb TO myprojectuser;`
# - Exit the shell using: `\q`


#4. Installing psycopg2 (PostgreSQL adapter for Python)
# - Django uses this as a driver to talk to PostgreSQL.
# - Run: pip install psycopg2-binary


#5. Configure Django to use PostgreSQL
# - Open settings.py and update DATABASES:
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myprojectdb',
        'USER': 'myprojectuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
'''


#6. Apply Migrations
# - Now apply migrations so PostgreSQL has all your tables: python manage.py migrate
# - This will create all Django tables (users, auth, sessions, etc.) in PostgreSQL.


#7. Test the Connection 
# - Create a superuser in PostgreSQL DB: python manage.py createsuperuser
# - Run the server: python manage.py runserver
# - Visit http://127.0.0.1:8000/admin/
# - Log in with the superuser credentials to verify everything is working.


#8. Best Practices
# - Never hardcode passwords in settings.py; use environment variables:
'''
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
'''
# - Store credentials in a .env file and use python-decouple or django-environ to load them.
# - For production, ensure PostgreSQL accepts remote connections securely (SSL, firewalls).