#1. What Are Static Files?
# - Static files are assets like:
        # - CSS files for styling
        # - JavaScript files for interactivity
        # - Images like logo, icons, etc.
# - They do not change dynamically and are served as-is
#   to the browser.


#2. Configuring Static Settings
# - Django needs to know where to find your static files.
# - Open mysite/settings.py and check these settings:
'''
# Already present
STATIC_URL = '/static/'

# Optional for organizing your static files
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
'''   


#3. Creating a Static Directory
# - At the project level (same level as manage.py), create:
'''
static/
└── css/
    └── style.css
'''
# - Inside style.css, add:
'''
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    color: #333;
}

h1 {
    color: #0059b3;
}
'''


#4. Using Static Files in a Template
# - In any HTML template (e.g., home.html, word_counter.html), do the following:
#i. Load static files at the top of the template:
'''
{% load static %}
'''
#ii. Link the CSS file in the <head>:
'''
<link rel="stylesheet" href="{% static 'css/style.css' %}">
'''

#iii. Final Template Example:
'''
<!-- home/templates/home/home.html -->
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <h1>Welcome to the Home Page</h1>
    <p>This page is now styled with CSS!</p>
</body>
</html>
'''


#5. Using Static Images
# - Let's say you have:
'''
static/
└── images/
    └── logo.png
'''
# - In your template:
'''
<img src="{% static 'images/logo.png' %}" alt="Logo" width="100">
'''


#6. Static Files in Apps (Alternative)
# - You can also put static files inside an app like this:
'''
home/
└── static/
    └── home/
        └── custom.css
'''
# - Then load with:
'''
<link rel="stylesheet" href="{% static 'home/custom.css' %}">
'''

# - ✅ Best practice: Use project-level static folder for global styles, 
#       and app-level for app-specific styles.


#  - Run the Server and Test 
'''
python manage.py runserver
'''
# - Visit your page. It should now be styled using your custom CSS!


# Summary
#   ----------------------------------------------------------------------------------- 
#   | Task            | Code                                                          |
#   | --------------- | ------------------------------------------------------------- |
#   | Load static tag | `{% load static %}`                                           |
#   | CSS file        | `<link rel="stylesheet" href="{% static 'css/style.css' %}">` |
#   | JS file         | `<script src="{% static 'js/script.js' %}"></script>`         |
#   | Image           | `<img src="{% static 'images/logo.png' %}" alt="Logo">`       |
#   ----------------------------------------------------------------------------------- 

# ✅ Best Practices:
# - Always use {% load static %} at the top of templates using static files
# - Organize static files by type: /css/, /js/, /images/
# - Don’t use absolute URLs; always use {% static %} for portability