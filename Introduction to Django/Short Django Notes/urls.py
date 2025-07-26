# Understanding urls.py Django

#1. What is urls.py?
# - It's the URL configuration file for your Django project or app.
# - It tells Django: “When a user visits a certain URL, which view
#   should handle it?”


#2. Real-life analogy
# - Imagine Django is a call center, and urls.py is the receptionist’s
#   directory. When someone calls (visits a URL), urls.py tells Django
#   which department (view function) should pick up the call (respond).


#3. Types of urls.py
# - Django uses two levels of URL configuration:

#i. Project-level urls.py
# - Located in the folder named after your project (e.g., mysite/urls.py),
#   where 'mysite' is your project's name.
# - Purpose:
    # - Routes high-level URLs.
    # - Connects to app-level URL configurations using include().

#ii. App-level urls.py
# - Located inside your Django app (e.g., pages/urls.py)
# - Purpose:
    # - Defines app-specific URL routes (e.g., home page, about page).

#   How They Work Together
# - Django checks URLs in this order:
#   Browser visits --> Project urls.py --> App urls.py --> View --> Template/Response

# - Example 1: Project-level urls.py
'''
# mysite/urls.py

from django.contrib import admin
from django.urls import path, include  # include lets us connect to app urls

urlpatterns = [
    path('admin/', admin.site.urls),  # admin/ is for Django’s admin site
    path('', include('pages.urls')),  # when the base URL is visited, go to pages app
]                                     # base URL is represented by empty string ('') 
                                      # include('pages.urls'): delegates routing to the pages app  

'''

# - Example 2: App-level urls.py
'''
# pages/urls.py

from django.urls import path
from . import views  # import views from current app

urlpatterns = [
    path('', views.home, name='home'),           # route for "/" ("/" is the base URL)
    path('about/', views.about, name='about'),   # route for "/about/"
]

'''
# - The code above tells Django to call views.home() for /, and views.about() for /about/

# - path() Function: Simple Breakdown
'''
path('about/', views.about, name='about')
'''
    # - 'about/': URL path (what user types in the browser)
    # - views.about: view function that handles the request
    # - name='about': optional name for this URL (used in templates for linking)

# - Using include()
#   This lets you break up large projects into apps and keep their URL logic separate.
'''
# mysite/urls.py
urlpatterns = [
    path('', include('blog.urls')),  # send all requests to blog app
]

'''
'''
# blog/urls.py
urlpatterns = [
    path('', views.index),
    path('post/', views.post_detail),
]

'''


#  Example: Dynamic URLs with Parameters
# - Purpose: Pass values in the URL (e.g., instagram.com/user/23)
'''
# blog/urls.py
path('post/<int:id>/', views.post_detail, name='post-detail')

'''
#'<int:id>': captures an integer from the URL and passes it to the view

# - View Function:
'''
def post_detail(request, id):
    return HttpResponse(f"Viewing post with ID {id}")

'''
# - URL:
    # http://127.0.0.1:8000/post/10/ → output: “Viewing post with ID 10”


# - Best Practices for URL Configuration
#1. Use app-level urls.py files:	        Keeps each app's routing clean
#2. Name your URLs (name='home'):	        Makes them reusable in templates with {% url 'home' %}
#3. Avoid hardcoding links:	                Use {% url 'name' %} in templates
#4. Use dynamic routes for IDs, slugs:	    Clean, RESTful URL design
#5. Use include() in project/urls.py:	    Keeps the root URL config simple
#6. Add trailing slashes (/):           	Consistent with Django’s URL style