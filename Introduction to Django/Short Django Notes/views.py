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
