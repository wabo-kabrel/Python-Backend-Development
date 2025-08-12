#   Twitter Bootstrap Integration with Flask-Bootstrap
#1. What is Bootstrap?
# - Bootstrap is an open-source UI framework from Twitter.
# - It helps developers build clean, responsive, and attractive web pages quickly by providing:
    # - Pre-styled CSS components (buttons, forms, grids, navbars, etc.)
    # - JavaScript plugins for interactivity
    # - Compatibility with all major browsers
# - 💡 Bootstrap is purely client-side → it’s HTML/CSS/JS, not Python. Flask only needs to send
#   HTML that includes Bootstrap’s files.


#2. Why Flask-Bootstrap?
# - Normally, to use Bootstrap, you would:
    # - Download or link Bootstrap CSS and JS files in your HTML
    # - Structure your HTML to match Bootstrap’s component styles
# - But Flask-Bootstrap is a Flask extension that makes this much easier:
    # - Automatically includes all required Bootstrap files in your templates
    # - Provides a base template with Bootstrap already integrated
    # - Lets you extend that base instead of writing all the boilerplate yourself

# - 📦 Install it:  `pip install flask-bootstrap`


#3. Initialization
# - Just like other Flask extensions:
'''
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
'''
# - Here:
    # - Bootstrap(app) registers Bootstrap with your Flask app
    # - Now you can use bootstrap/base.html as your parent template


#4. Using the Base Template
# - Flask-Bootstrap’s bootstrap/base.html contains:
    # - HTML skeleton
    # - <head> section with Bootstrap CSS
    # - <body> with proper structure
    # - Placeholder blocks for you to override
# - Example(templates/user.html):
'''
{% extends "bootstrap/base.html" %}

{% block title %}Flasky{% endblock %}

{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle"
                    data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">Flasky</a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/">Home</a></li>
            </ul>
        </div>
    </div>
</div>
{% endblock %}

{% block content %}
<div class="container">
    <div class="page-header">
        <h1>Hello, {{ name }}!</h1>
    </div>
</div>
{% endblock %}
'''


#5. Template Inheritance
# - {% extends ... %} → tells Jinja2 to use the Bootstrap base template
# - {% block ... %}{% endblock %} → defines what goes in certain sections
# - bootstrap/base.html defines many blocks you can override:
    # | Block Name                | Purpose                      |
    # | ------------------------- | ---------------------------- |
    # | `title`                   | Page `<title>` text          |
    # | `navbar`                  | Navigation bar content       |
    # | `content`                 | Main page content            |
    # | `scripts`                 | JavaScript at bottom of page |
    # | `styles`                  | CSS declarations             |
    # | `metas`                   | Meta tags                    |
    # | `body_attribs`            | `<body>` tag attributes      |
    #  … plus many internal ones                               


#6. Adding Extra Content to a Block
# - If you override a block that already has default content (like scripts or styles), 
#   you should keep the original content by calling:
'''
`jinja2`

{% block scripts %}
    {{ super() }}
    <script src="my-script.js"></script>
{% endblock %}
'''
# - Here:
    # - {{ super() }} → includes whatever was in the base template’s scripts block
    # - Then you append your own <script> tag


#7.  Example in Action
# - If your name is "Alice" and you visit /user/Alice, the rendered HTML might look like:
'''
<!doctype html>
<html lang="en">
<head>
    <title>Flasky</title>
    <link rel="stylesheet" href="/static/bootstrap.min.css">
</head>
<body>
    <div class="navbar navbar-inverse"> ... </div>
    <div class="container">
        <div class="page-header">
            <h1>Hello, Alice!</h1>
        </div>
    </div>
    <script src="/static/bootstrap.min.js"></script>
</body>
</html> 
'''
