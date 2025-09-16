# Basic Concepts

# - Project: Refers to the entire web application.
# - App: A component of the project with specific functionality.
# - The project can be thought of as a school, and the apps as classrooms within the school.
# - For an application like Instagram, Instagram is considered the project while
#the apps include the notifications section, the DM section, the profile section,
#the reels section, etc.

# Creating an App and Routing URLs
# - Before creating an app, ensure you're in the root directory of your Django project.
# - The root directory is where the `manage.py` file is located.
# - Run the command `python manage.py startapp myapp` to create a new app.
# - Replace `myapp` with the desired name for your app.
# - This command creates a folder named `myapp` in the current directory, with structure:
'''myapp/
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py       ← Write your logic here
├── urls.py        ← You’ll create this manually
└── __init__.py
'''