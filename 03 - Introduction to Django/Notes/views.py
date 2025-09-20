#1. Views in Django
# - A view is a Python function (or class) that tells Django 
# what to do when a user visits a specific page (URL).
# - Example: When someone visits instagram.com/home, a view decides what
# to show on that page (like your feed).

# - In Django, you define these views in a file called views.py.
# - Example of a simple view:
'''
# pages/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage!")
''' 
# - home is a view function.
# - When called(requested), it returns plain text: "Welcome to the homepage!"


#2. How Views Connect to URLs and Templates
# - Views are connected to URLs using a file called urls.py.
# - This file maps URLs to specific views.
# - Example:
'''
# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
'''
# - So when a user goes to http://127.0.0.1:8000/, Django runs the home() view.
# - You can also use render() to return an HTML page:
'''
# views.py

from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')
'''


#3. Types of Views
# - Function-Based Views (FBV) – simple, beginner-friendly. Example:
'''
def hello(request):
    return HttpResponse("Hello, world!")
'''

# - Class-Based Views (CBV) – more powerful and reusable. Example:
'''
from django.views import View
from django.http import HttpResponse

class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello from a class-based view!")
'''
# In urls.py:
'''
path('hello/', HelloView.as_view(), name='hello')
'''


#4. Returning HTML Pages and Data
# - Basic HTML view:
'''
def home(request):
    return render(request, 'pages/home.html')
'''

# - Passing Dynamic Data:
'''
def about(request):
    context = {
        'developer': 'Kabrel Wabo',
        'year': 2025,
    }
    return render(request, 'pages/about.html', context)
'''
# In about.html:
'''
<p>This site was built by {{ developer }} in {{ year }}.</p>

'''

#5.  Handling User Input: GET vs POST
#i. GET Request:
# - Used to retrieve (ask for) data from the server.
# - Example: When you type a URL in your browser, it sends a GET request.

#ii. POST Request:
# - Used to send data to the server, like when you submit a form.
# - Example: When you fill out a form and click "Submit", it sends a POST request.

# - Example: Handling a form in a View
'''
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f"Thanks, {name}!")
    return render(request, 'pages/contact.html')

'''
# In contact.html:
'''
<form method="post">
    {% csrf_token %}
    <input type="text" name="name" placeholder="Your name">
    <button type="submit">Send</button>
</form>
'''

# - {% csrf_token %} protects your form from hackers using
# Cross-Site Request Forgery attacks.


#6. Best Practices for Writing Views
# - Keep views clean and simple: Don't put too much logic in them.
# - Use templates: Return full HTML using render(), not HttpResponse
#  unless needed.
# - Use context: Pass data to templates using dictionaries.
# - Use CBVs for complex logic: Class-based views are better for advanced pages like 
#   forms, APIs, etc.
# - Use meaningful names: 	Name your views clearly, e.g., user_profile, dashboard, etc.


#   How Views Fit Into the Django Flow
''' User visits /about/ → URLconf finds views.about → 
    views.about() runs → render() returns HTML → Page shows in browser
'''
