#1.  Why Templates Exist
# - In Flask, a view function often needs to:
    # - Do business logic: Update the database, process user input, etc.
    # - Do presentation logic: Format the response HTML for the browser.
# - If we mix those in one big Python string (e.g., "<h1>Hello %s</h1>" % name),
#   the code quickly becomes ugly and hard to maintain.
# - Templates solve this by separating presentation logic (HTML) from business logic (Python code).
    # - Python handles the data
    # - Templates handle how that data is displayed


#2. How Templates Work in Flask
# - Flask uses the Jinja2 template engine to render templates.
# - A template is just an HTML (or other text) file with placeholders like
#   {{ variable }} for dynamic values.
# - Basic example:
# In templates/user.html:
'''
<h1>Hello, {{ name }}!</h1>
'''
# In app.py:
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
'''
    # - render_template('user.html', name=name)
        # → loads the file from the templates folder
        # → replaces {{ name }} with the actual value.


#3. Variables in Templates
# You can insert any Python variable type into a template:
'''
`html`

<p>{{ username }}</p>
<p>{{ mylist[0] }}</p>
<p>{{ mydict['key'] }}</p>
<p>{{ myobject.method() }}</p>
'''

#4. Filters — Modifying Variables
# - Filters use a pipe (|) to transform data:
# - Example:
'''Hello, {{ name|capitalize }}
'''

# Common Filters
# | Filter       | Effect                                                          |
# | ------------ | --------------------------------------------------------------- |
# | `safe`       | Render without escaping HTML (⚠ dangerous with untrusted input) |
# | `capitalize` | First letter uppercase, rest lowercase                          |
# | `lower`      | All lowercase                                                   |
# | `upper`      | All uppercase                                                   |
# | `title`      | Capitalize each word                                            |
# | `trim`       | Remove whitespace at start/end                                  |
# | `striptags`  | Remove HTML tags                                                |


#5. Control Structures
# - Jinja2 supports Python-like control flow inside templates.
# - Conditionals
'''
`html`

{% if user %}
    Hello, {{ user }}!
{% else %}
    Hello, Stranger!
{% endif %}
'''
# - Loops
'''
`html`

<ul>
{% for comment in comments %}
    <li>{{ comment }}</li>
{% endfor %}
</ul>
'''


#6. Macros (Reusable Template Functions)
# - Like functions in Python, but for templates:
'''
`html`

{% macro render_comment(comment) %}
    <li>{{ comment }}</li>
{% endmacro %}

<ul>
{% for c in comments %}
    {{ render_comment(c) }}
{% endfor %}
</ul>
'''
# - You can also import macros from other files
'''
`html`

{% import 'macros.html' as macros %}
{{ macros.render_comment("Nice post!") }}
'''
# To render means to take a template (like an HTML file with placeholders) and
# combine it with data to produce a final HTML page that the browser can display.


#7. Includes
# - Lets you reuse common pieces of HTML:
'''
`hmtl`

{% include 'navbar.html' %}
'''


#8. Template Inheritance
#i. Create a base template (base.html):
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # No variables

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)  # Pass variables
'''

#ii. Create a child template:
'''
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block body %}
<h1>Welcome!</h1>
{% endblock %}
'''

#iii. How it works:
# - {% block %} → placeholders that child templates can override.
# - {% extends %} → tells Jinja2 to start with base.html.
# - {{ super() }} → keep original block content and add to it.


#9.  Rendering Templates in Flask
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # No variables

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)  # Pass variables
'''

# Note:
    # - Templates must be in a templates/ folder.
    # - Variables are passed as keyword arguments to render_template.

