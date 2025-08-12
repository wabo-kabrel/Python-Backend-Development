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