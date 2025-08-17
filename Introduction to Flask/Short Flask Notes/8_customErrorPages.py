#1. Why Custom Error Pages?
# - By default, Flask sends you a plain, ugly HTML error page if:
    # - You go to a route that doesn't exist (404 Not Found)
    # - Your app crashes unexpectedly (500 Internal Server Error)
# - Problem:
    # These default pages look nothing like the rest of your site — no navigation
    # bar, no styling, no brand identity.
# - Solution:
    # We override these defaults with custom handlers that:
    # - Use templates (so they look like the rest of your site)
    # - Can use Bootstrap or your own CSS for styling
    # - Can be reused for multiple error types


#2. How to Create Custom Error Pages
# - Flask lets you "catch" certain HTTP errors and run your own function for them
#   using @app.errorhandler().
# - Example:
'''
from flask import render_template

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
'''
# What's happening here?
# - @app.errorhandler(404) means: "Whenever a 404 happens, run this function."
# - The function:
    # - Uses render_template() to return a nice HTML page.
    # - Returns the status code as the second argument so the browsers still know it's an
    #   error.
# - The same idea works for 500 or any other error code.


#3. Avoiding Repetition with Template Inheritance
# - You could just copy your user.html and change the message for 404.html 
#   and 500.html, but that’s wasteful.
# - If you change your navbar later, you’d have to update every single page.
# - Instead:
    # - Create a base template with your shared layout (navbar, Bootstrap CSS, footer)
    # - Let other templates inherit from it
    # - Override only the content that changes

# Base Template (templates/base.html)
'''
`jinja2`

{% extends "bootstrap/base.html" %}

{% block title %}Flasky{% endblock %}

{% block navbar %}
<div class = "navbar navbar-inverse" role = "navigation">
    <div class = "container">
        <div class = "navbar-header">
            <a class = "navbar-brand" href = "/">Flasky</a>
        </div>
        <ul class = "nav navbar-nav">
            <li><a href = "/">Home</a></li>
        </ul>
    </div>
</div>
{% endblock %}

{% block content %}
<div class = "container">
    {% block page_content %}{% endblock %}
</div>
{% endblock %}
'''
# Key ideas:
    # - This inherits from Bootstrap's own base template (so we get CSS/JS automatically).
    # - It defines the navbar once
    # - It defines a {% block page_content %} for each page to insert its own unique content.

# Custom 404 Page (templates/404.html)
''' 
`jinja2`

{% extends "base.html" %}

{% block title %}Flasky - Page Not Found{% endblock %}

{% block page_content %}
<div class = "page-header">
    <h1>Not Found</h1>
    <p>Sorry, we couldn't find the page you were looking for.</p>
</div>
{% endblock %}
'''

# Custom 500 Page (templates/500.html)
'''
`jinja2`

{% extends "base.html" %}

{% block title %}Flasky - Server Error{% endblock %}

{% block page_content %}
<div class="page-header">
    <h1>Internal Server Error</h1>
    <p>Something went wrong. We’re working on it!</p>
</div>
{% endblock %}
'''


#4. Benefits
# - Consistent look — Error pages match your site’s theme
# - Easier maintenance — Change the navbar in base.html and it updates everywhere
# - Better user experience — No jarring default error screens


#5. Quick Mental Model
# You can think of it like this:
    # - Without inheritance: You write your whole HTML from scratch for each error page.
    # - With inheritance: You just “fill in the blank” for the unique part, and let 
    #   the rest come from a shared template.