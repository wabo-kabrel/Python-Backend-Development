# Sending/Passing Data to Template File

#1. Why Pass Data to Template?
# - Templates display content to the user (HTML pages).But HTML alone is static. 
#   You pass data from views.py to make your pages dynamic, like:
    # - Showing a user’s name
    # - Listing blog posts
    # - Displaying a success message after form submission


#2. The Basic Flow
# - View (Python code) ➡ passes data ➡ to Template (HTML with DTL)


#3. Example 1: Passing Simple Variables
#i. In views.py:
'''
from django.shortcuts import render

def greet_user(request):
    context = {
        'name': 'Kabrel',
        'age': 23
    }
    return render(request, 'pages/greet.html', context)
'''
    # - context: A Python dictionary with data to send to the HTML page.
    # - 'name' and 'age' are keys; 'Kabrel' and 23 are values.
    
#ii. In templates/pages/greet.html:
'''
<h1>Hello, {{ name }}!</h1>
<p>You are {{ age }} years old.</p>
'''
    # - {{ name }} and {{ age }} are Django Template Language (DTL) variables.
    # - Django replaces them with the values passed from the view.


#4. Example 2: Passing a List 
#i. In views.py:
'''
def services(request):
    context = {
        'services': ['Web Design', 'SEO', 'Django Development']
    }
    return render(request, 'pages/services.html', context)
'''
#ii. In services.html:
'''
<h2>Our Services</h2>
<ul>
  {% for service in services %}
    <li>{{ service }}</li>
  {% endfor %}
</ul>
'''
    # - {% for service in services %} is a loop tag.
    # - It loops through the list and prints each item.


#5. Example 3: Passing a Dictionary
#i. In views.py:
'''
def profile(request):
    context = {
        'user': {
            'name': 'Kabrel',
            'email': 'kabrel@example.com'
        }
    }
    return render(request, 'pages/profile.html', context)
'''
#ii. In profile.html:
'''
<h2>User Profile</h2>
<p>Name: {{ user.name }}</p>
<p>Email: {{ user.email }}</p>
'''


#6. Example 4: Conditional Statements
#i. In views.py:
'''
def login_status(request):
    context = {
        'is_logged_in': True
    }
    return render(request, 'pages/status.html', context)
'''
#ii. In status.html:
'''
{% if is_logged_in %}
  <p>Welcome back!</p>
{% else %}
  <p>Please log in.</p>
{% endif %}
'''

#7. Best Practices
# - Use descriptive variable names:	        Improves readability
# - Keep views clean:                       Only prepare and pass data; don’t write HTML in views
# - Keep context organized:                 Use dictionaries
# - Don’t hardcode values in templates:     Pass them from views for flexibility
# - Use {% csrf_token %} for forms: 	    Protects from security attacks