# Django Template Language (DTL)

# - A template is a regular HTML file, but it can also contain Django
#   code (called Django Template Language or DTL).
# - Instead of sending boring plain text with HttpResponse, we use render()
#   to display full HTML pages with dynamic data.
# - Templates are stored in a folder called templates, which is inside the app folder.
# - The render() function takes the request, the template name, and a context dictionary
#   as arguments and returns an HttpResponse object with the rendered template.


#  Step-by-Step: Setting Up Templates in Django
#1.
# - Create a `templates` folder the root directory of your Django project.
# - Your file structure should look like this:
#   ```
#   myproject/
#   ├── myproject/
#   ├── manage.py
#   ├── templates/

#2. Create an HTML Template
# - File: pages/templates/pages/home.html
'''
<!DOCTYPE html>
<html>
<head>
    <title>My Django Site</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
    <p>Welcome to the homepage.</p>
</body>
</html>
'''
# - {{ name }} is a placeholder for dynamic data passed from the view.

#3. Update Your View to Use render()
# - In views.py, import render and update your view function:
'''
from django.shortcuts import render

def home(request):
    context = {
        'name': 'Kabrel'
    }
    return render(request, 'pages/home.html', context)
'''
# - render() tells Django: “Find this HTML template and fill it with data.”
# - context is a Python dictionary (key: value) where the keys become variables in 
#   your template.

#4. Update Your URL Configuration
# - In urls.py, ensure your view is mapped correctly:
'''from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    # Add other URL patterns here if needed
]
'''
# - This maps the root URL to the home view.

#5. Run the Server and Test
# - Start your Django development server using the command:
#   `python manage.py runserver`
# - Visit http://127.0.0.1:8000/ in your browser to see your template in action.
# - You should see "Hello, Kabrel!" displayed on the page.


# Django Template Language (DTL) Basics
# - Here are the most important features of DTL:
#1. Variable Output
# - Used to display dynamic data in templates.
# - Example:
'''
<h1>Hello, {{ name }}!</h1> 
'''
# - This will output the value of the `name` variable passed from the view.

#2. If Statements
# - Used for conditional rendering.
# - Example:
'''
{% if user %}
    <p>Welcome, {{ user }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
'''
# - This checks if the `user` variable exists and displays a welcome message or a prompt to log in.

#3. For Loops
# - Used to iterate over lists or dictionaries.
# - Example:
'''
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
'''
# - This will create a list item for each `item` in the `items` list.
# - Example View:
'''
def list_view(request):
    context = {
        'items': ['Apples', 'Bananas', 'Cherries']
    }
    return render(request, 'pages/list.html', context)
'''
# - This view passes a list of items to the template, which will be displayed as a list.

#4. Template Inheritance
# - Allows you to create a base template and extend it in other templates.

#5. Comments
# - Used to add comments in templates that won't be rendered in the final HTML.
# - Example:
'''
{# This is a comment #}
'''

# How Templates Work in Django
# - User visits → URL → View → render(template, context) → HTML response
