#1. What is Flask?
# - Flask is a lightweight, flexible Python web framework that provides
#   the basic tools to build web applications and APIs (REST APIs).
# - Unlike Django (a "batteries-included" framework), Flask follows a minimalist
#   approach, giving you the freedom to choose your components.


#2. Key Features of Flask
# - Micro-framework: Minimal core with extensions
# - Flexible: Choose your own database, templating engine, etc.
# - WSGI-based: Web Server Gateway Interface compatible
# - Jinja2 templating: Powerful template engine
# - Werkzeug toolkit: HTTP utilities and debugging


#3. Flask vs Other Frameworks:
# - Django: More opinionated, includes ORM, admin panel
# - FastAPI: Modern, async-first, automatic API documentation
# - Flask: Middle ground - simple but extensible


#4. Setting Up Your Flask Environment
#i. Step 1: Create a Virtual Environment
'''
# Create project directory
mkdir flask-course
cd flask-course

# Create virtual environment
python -m venv flask-env

# Activate virtual environment
# On Windows:
flask-env\Scripts\activate
# On macOS/Linux:
source flask-env/bin/activate
'''

#ii. Step 2: Install Flask

# - Run `pip install Flask` in the terminal in the project directory

# - Optional: Install Flask extensions
        # - Run `pip install Flask-SQLAlchemy Flask-Migrate Flask-WTF`
        # - Flask-SQLAlchemy: ORM for database interactions
        # - Flask-Migrate: Database migrations
        # - Flask-WTF: Form handling and validation

#iii. Step 3: Verify Installation
# - Run `python -m flask --version` to check Flask version
# - You should see output like:
# ```
# Flask 2.0.1
# ```
# - If you see an error, ensure your virtual environment is activated and Flask is installed.


#5. Creating a Simple Flask Application
# - Create a new file named `app.py` in your project directory
# - Add the following code to `app.py`:
'''
from flask import Flask

app = Flask(__name__)       # an instance of the Flask class. The web server 

@app.route('/')
def home():                     # view function
    return "Hello, Flask!"      # a simple route that returns a string. When a client sends a 
                                  a request to the slash ('/'), the home function is called and it returns "Hello, Flask!" as a response.
'''
# - Run the application using `flask run` in the terminal