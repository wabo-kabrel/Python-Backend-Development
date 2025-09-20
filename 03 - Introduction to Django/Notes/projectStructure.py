
# Django Project Structure

'''
        
        mysite/        ←  Root directory of the Django project
├── manage.py          ← CLI tool to run Django commands
├── mysite/            ← Project directory containing settings and configuration
│   ├── __init__.py    ← Marks the directory as a Python package
│   ├── settings.py    ← Project settings and configurations
│   ├── urls.py        ← Root URL declarations for the project
│   ├── asgi.py        ← ASGI application for deployment
│   └── wsgi.py        ← WSGI application for deployment

'''

# Create a Django project

# - Run the command "django-admin startproject myproject" without the "". 
# - Navigate to the project using "cd myproject"
# - myproject is the name of the project in this case, and the project
# created will have the project structure shown above.

# - Run the command "python manage.py runserver" without the "" to run
# the development server.
# - Now,visit the localhost http://127.0.0.1:8000/ to see the Django welcome page.

# Run "pip freeze > requirements.txt" to create the requirements file.

# Best Practices
# - Always use a virtual environment to keep dependencies isolated per project.
# - Install dependencies in requirements.txt using the previous command. These
#dependencies help with version control.
# - Avoid editing core Django files. Customize through apps and settings instead.


