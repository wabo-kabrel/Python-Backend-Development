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
#i. 
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
# - Open your web browser and visit `http://127.0.0.1:5000/` (the localhost address)
# - You should see "Hello, Flask!" displayed in your browser

#ii. Understanding the Code:
# - When a client makes a request by visiting the website (localhost in this case),
#   the web server receives and passes the request to the object `app` (an instance
#   of the Flask class), using the WSGI protocol.
# - The `@app.route('/')` decorator tells Flask to execute the `home` function whenever
#   a request is made to the root URL ('/').

#iii. Definition of key terms used:
# - Route: A URL pattern that maps to a specific function in your application.
# - View Function: A function that handles a request and returns a response.
# - Decorator: A special syntax in Python that allows you to modify the behavior of a function or method.
# - Instance: An object created from a class. In this case, `app` is an instance of the Flask class.
# - WSGI: Web Server Gateway Interface, a standard interface between web servers and Python web applications.
# - HTTP: Hypertext Transfer Protocol, the protocol used for communication between clients and servers.
# - URL: Uniform Resource Locator, the address used to access resources on the web.
# - Response: The data sent back to the client after processing a request.
# - Request: The data sent by the client to the server when accessing a resource.
# - Client: The entity (usually a web browser) that makes requests to the server.
# - Server: The entity that processes requests and sends responses back to the client.