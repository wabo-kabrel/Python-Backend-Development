#1. How Django Handles Sessions
# - When a user log in:
    # - Django creates a session ID and stores it in the database.
    # - A session cookie is placed in the browser.
    # - The cookie links to the user's session data. Django knows which user is logged in by checking this cookie.

# - When the user logs out:
    # - The cookie is deleted, clearing the session.


#2. Add Login and Logout URLs (Built-in Way)
# - Django already provides login/logout views in django.contrib.auth.views
# - In accounts/urls.py, add:
'''
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
]
'''


#3. Create Login Template
# - In accounts/templates/accounts/login.html,
'''
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
    </form>
</body>
</html>
'''
# - The login view automatically provides a form (username + password).


#4. Create a Logout Link
# - Add this anywhere in your templates (e.g. in a navbar):
'''
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
    <a href="{% url 'logout' %}">Logout</a>
{% else %}
    <a href="{% url 'login' %}">Login</a> | 
    <a href="{% url 'register' %}">Register</a>
{% endif %}
'''


#5. Settings for Login/Logout Redirects
# - In settings.py, you can specify where to redirect users after login/logout:
'''
LOGIN_REDIRECT_URL = "/"   # where to go after login
LOGOUT_REDIRECT_URL = "login"  # where to go after logout
'''


#6. (Optional) Custom Login View
# - If you want more control (e.g. adding messages):
# - In accounts/views.py:
'''
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def custom_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "accounts/login.html")

def custom_logout(request):
    logout(request)
    return redirect("login")
'''
# - You would then replace the built-in LoginView and LogoutView with these in your urls.py.


#7. Testing
# - Run the server and register a new user at /accounts/register/
# - Login at /accounts/login/
# - See the welcome message
# - Logout at /accounts/logout/
