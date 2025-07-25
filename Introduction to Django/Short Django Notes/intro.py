# Django is a high-level Python web framework that allows rapid development of 
# secure and maintainable websites.

# Key Features:
# - MTV Architecture: Django follows the Model-Template-View pattern.
# - ORM: Object-Relational Mapping for database interactions.
# - Admin Interface: Automatically generated admin interface for models.
# - URL Routing: Clean and elegant URL routing.
# - Middleware: Process requests globally before reaching views.
# - Security: Built-in protection against common web vulnerabilities.
# - Scalability: Designed to handle high traffic and large applications.
# - Community: Large ecosystem with many reusable apps and libraries.
# - Documentation: Comprehensive documentation and tutorials available.

# Foundational Concepts in Django & Backend Development

#1. Project: 
# - The entire web application or website, which can contain multiple apps.
# - Created with `django-admin startproject mysite`

#2. App: 
# - A self-contained module within a project that provides specific functionality.
# - Example: You might have an app for user authentication, another for blog posts, etc.
# - Created with `python manage.py startapp myapp` where myapp is the name of your app.

#3. Model:
# A model defines the structure of your data.  Think of it like a blueprint for a 
# database table. Example:
'''
# models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

'''
# This creates a table called Post with title, body, and created columns in your database.

#4. URL (Uniform Resource Locator): The web address you type in your browser to visit
# a page. Ex: https://instagram.com/
# You define which URL connects to what page using urls.py. Example:
'''
    # pages/urls.py
    path('about/', views.about)      
'''
# The line of code above means that when someone visits /about/, Django
# will run the about() function in views.py.

#5. Views: 
# A view is the function or class in Django that receives a request and
# returns a response. It decides: “What should the user see when they visit this page?”
# It is connected to a URL in urls.py.
# Example of a view function:
'''    # pages/views.py
from django.http import HttpResponse

def about(request):
    return HttpResponse("This is the About page")
'''
 
#6. Route:
# A route (or URL pattern) is just the path in the URL that points to the view.
# Example:
'''path('about/', views.about)'''
# 'about/' is the route. When the browser hits this route, Django calls views.about().

#7. Template:
# A template is a file (usually HTML) that controls how the page looks.
# Instead of running plaintext (HttpResponse), we return HTML templates for real web pages.
# Example:
'''
# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

''' 
# The code above tells Django: "Render the file home.html from the templates/pages/ folder."
# You can insert dynamic content into templates using Django Template Language.

#8. HTTP (Hypertext Transfer Protocol):
# HTTP is the language of the web. It's how your browser talks to the server
# using requests and gets responses.

#9. GET and POST Methods:
#i. GET:
# - Used when you want to get data (like visiting a webpage).
# - Data is sent in the URL (like search queries).
# - Example: Visiting instagram.com/explore is a GET request.

#ii. POST:
# - Used when you want to send data to the server (like submitting a form).
# - Data is sent in the body of the request, not in the URL.
# - Example: When you log in or register, you POST your username and password.
'''
def login_view(request):
    if request.method == 'POST':
        # Handle form submission
        ...
    else:
        # Show empty login form
        ...

'''
# - You check request.method to see if the form was submitted or not.

#10. Request and Response:
# - A request is when the user (via a browser) asks for something from the server.
# - A response is what Django sends back(HTML page, JSON, error, etc.)
# Example:
'''
def home(request):  # ← request object from the browser
    return HttpResponse("Hello, World!")  # ← response
'''

#11. Admin Panel
# - A built-in Django feature that gives you a dashboard to view and
# edit your database.
# - Access it at `http://127.0.0.1:8000/admin/`
# - Register your models in admin.py to manage them through the admin interface.
# Example:
'''
from .models import Post
admin.site.register(Post)
'''

#12. Migration
# - When you make changes to models (like adding fields), Django 
# needs to update the database. This is done with migrations.
# - Common commands used:
'''
python manage.py makemigrations  # Create the migration file
python manage.py migrate         # Apply the changes to the database
'''