# Why Links Matter
# When your Flask app grows, you'll have multiple routes (pages). You 
# need a way to connect these routes together using links (like a navbar, 
# buttons, or references inside text).

# If you hardcore URLs inside templates, it works for small apps but quickly becomes
# a problem:
    # - If you change a route in app.py, you also have to manually update all the 
    #   templates that use it.
    # - Dynamic routes (like /user/<name>) are tricky to write directly.
# Flask gives us url_for() to generate links automatically, so they always stay in sync
# with the routes in your Python code.


# url_for() Basics
# - url_for() builds the URL for a view function (route) by its function name, not the URL string.
# - Example:
'''
`python`

from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the homepage.'

@app.route('/user/<name>')
def user(name):
    return f'Hello, {name}!'
'''
# Now, inside a template:
'''
<a href="{{ url_for('index') }}">Home</a>
<a href="{{ url_for('user', name='john') }}">John's Page</a>
'''
# Output:
'''
<a href="/">Home</a>
<a href="/user/john">John's Page</a>
'''


#  🌍 Relative vs Absolute URLs
# - Relative URL (default):
#   url_for('index') → /
#   Good for internal navigation (browser links).
# - Absolute URL:
#   url_for('index', _external=True) → http://localhost:5000/
#   Useful for links shared outside the app (like emails).


# 🌀 Dynamic URLs
# - If your route has variables (like <name>), you pass them as arguments to url_for():
'''
`python`

url_for('user', name='john')
'''
# Output → /user/john


# 📌 Adding Query Parameters
# - You can also pass extra arguments (even if they’re not part of the route). They’ll go
#   into the query string:
'''
`python`

url_for('index', page=2)
'''
# Output → /?page=2


# 🧩 Example with Navigation Bar
'''
<ul>
  <li><a href="{{ url_for('index') }}">Home</a></li>
  <li><a href="{{ url_for('user', name='john') }}">John</a></li>
  <li><a href="{{ url_for('user', name='mary') }}">Mary</a></li>
</ul>
'''


# ✅ Key Benefits of url_for():
# - No broken links if you change route URLs.
# - Handles dynamic parameters easily.
# - Can generate both relative and absolute links.
# - Clean, maintainable, and consistent.