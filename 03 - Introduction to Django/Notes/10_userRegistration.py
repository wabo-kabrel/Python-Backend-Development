#1. How Authentication Works in Django
# Django has a built-in authentication system that manages:
    # - Users
    # - Groups
    # - Permissions
    # - Password hashing & validation
# It comes  with the User model(django.contrib.auth.models.User), which already includes:
    # - Username
    # - Email
    # - Password (hashed, not plain text)
    # - Fist/Last name
    # - Staff/admin status


#2. Creating a Registration App
# - It's best practice to create a separate app for authentication.
# - Run the command: python manage.py startapp accounts
# - Add 'accounts' to INSTALLED_APPS in settings.py


#3. Creating a Registration Form
# - Instead of building a form from scratch, we can extend Django's built-in UserCreationForm.
# - In accounts/forms.py:
'''
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
'''
# - This gives us a form with:
    # - Username
    # - Email
    # - Password
    # - Confirm Password


#4. Creating the Registration View
# - In accounts/views.py:
'''
from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect after successful registration
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})
'''


#5. Creating the Registration Template
# - In accounts/templates/accounts/register.html:
'''
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h2>Create an Account</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
</body>
</html>
'''
# - {{ form.as_p }} automatically renders the form fields with <p> tags.


#6. Configuring URL Routes
# - In accounts/urls.py:
'''
from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
]
'''

# - In project/urls.py:
'''
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("accounts.urls")),
    path("admin/", admin.site.urls),
]
'''


#7. Password Security in Django
# - Passwords are hashed using PBKDF2 by default.
# - Django automatically enforces password validation (minimum length, complexity, etc.).
# - Never store or log raw passwords.


#8. Testing the Registration System
# - Run the server: python manage.py runserver
# - Visit http://127.0.0.1:8000/accounts/register/
# - Register a new user and ensure
# - Check the database (via admin panel or shell) to confirm the user is created with a hashed password.
