# ⚡ What Are Static Files?
# In web applications, not everything is generated dynamically with Python and templates.
# We also use static files, which don’t change unless you manually edit them:
    # - CSS (stylesheets) 🎨
    # - JavaScript (client-side scripts) ⚙️
    # - Images (logos, icons, photos) 🖼️
    # - Fonts, PDFs, etc. 🔤
# These files are served directly by Flask when a browser requests them.


# 🛠️ Flask’s Static Route
# - Flask automatically provides a special route for static files:
''' /static/<filename>
'''
# - Example:
    # - /static/css/styles.css
    # - /static/js/app.js
    # - /static/images/logo.png


# 📂 Folder Structure
# - By default, Flask looks for static files in a folder named static/ inside your
#   project root.
# - Example project:
'''
myapp/
 ├── app.py
 ├── static/
 │    ├── css/
 │    │   └── styles.css
 │    ├── js/
 │    │   └── script.js
 │    └── images/
 │        └── logo.png
 └── templates/
      └── base.html
'''


# 🌍 Using url_for('static', filename=...)
# - Instead of hardcoding paths, we use url_for() to safely generate static file URLs.
# - Example:
'''
<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
<img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
'''
# - Flask will expand these into proper URLs like:
'''
/static/css/styles.css
/static/js/script.js
/static/images/logo.png
'''
# - If you change your app’s structure later, your links won’t break.


# 🌟 Example: Adding a Favicon
# - Inside templates/base.html:
'''
{% block head %}
  {{ super() }}
  <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}" type="image/x-icon">
  <link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}" type="image/x-icon">
{% endblock %}
'''
# - This tells the browser: "Hey, the favicon is stored at /static/favicon.ico."


# 🔑 Why Use url_for() Instead of Hardcoding?
# - Prevents broken links if routes change.
# - Works well with blueprints (modular apps).
# - Handles absolute URLs with _external=True.


# ✅ Quick Mini Example
# - app.py:
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
'''
# - templates/index.html:
'''
<!DOCTYPE html>
<html>
<head>
  <title>Flask Static Demo</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
  <h1>Hello, Flask with Static Files!</h1>
  <img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
  <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
'''
# - static/css/styles.css:
'''
body {
    background-color: lightblue;
    text-align: center;
}
'''
# 🔔 Now when you run the app, you’ll see styled text, a logo, and working 
# scripts — all powered by Flask’s static/ folder.