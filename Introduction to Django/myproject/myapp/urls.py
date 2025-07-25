# Purpose:
# The urls.py file inside an app routes (URLs) that map to
#specific view functions or class-based views within that app.
# While the project-level urls.py (in mysite/urls.py) acts as the main router,
# the app-level urls.py breaks the project into manageable components.

# This urls.py needs to be created manually after creating the app.

# Typical Content of urls.py

from django.urls import path # Imports the path() function used to define URL routes. 
                             # path() accepts: route, view, and name.   

from . import views         # Imports your local views module from the same folder (i.e., myapp/views.py).

urlpatterns = [
    path('', views.home, name='home'),
#    path('about/', views.about, name='about'),
]
