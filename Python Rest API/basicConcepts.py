#1. What is an API?
'''API stands for Application Programming Interface. It is like a waiter in a restaurant. You
(the client) ask for food (data), the waiter (API) takes your order to the kitchen (server), and
brings you the food (response).'''
# APIs allow two applications to talk to each other. E.g. Your phone app sends a request to a weather server.


#2. What is a REST API?
    # REST = Representational State Transfer.
    # REST is a style (not a technology) used to design networked applications.
    # Beginners can assume a REST API means an HTTP service that can be called 
    #using standard web libraries and tools. An API that doesn't do anything ("resting")
    #unless you call it.

# Key concepts in REST:
    # - Client: The user or frontend.
    # - Server: The backend that handles requests.
    # - Resources: Data entities like users, products, etc.
    # - HTTP Methods (verbs):
        # - GET: Read data.
        # - POST: Create new data.
        # - PUT: Update data.
        # - DELETE: Delete data.
    # - URLs: Identify resources (e.g., /users/1 is user with ID 1).
    # - JSON: Data is usually sent and received in JSON format.

# RESTful APIs follow these principles:
    # - Stateless: No client context is stored on the server.
    # - Uniform Interface: Same structure for interacting with resources.
    # - Use of HTTP methods properly.


#3. Tools Needed
    # - Python - the language
    # - Flask - a lightweight web framework
    # - Postman - for API testing
    # - Browser - for GET requests
    # - Virtual Environment (Optional) - Use a virtual environment in each project
    #in a repository to avoid dependency conflicts between the various projects.
    # Use the bash command: "py -m venv .venv" to create a virtual environment in a folder.
    # For each Flask API project, you need to install the Flask dependencies as shown in #4

#4. Installing Flask and other tools
    # - Use the bash command: pip install flask
    # - You can directly create a REST API using the bash command: pip install flask_restful.
    # - Use "pip install flask_sqlalchemy" to install the ORM (object relational mapping)
    #which will be used to talk to the database from the Python code.
    # - Use "pip freeze > requirements.txt" to create a requirement text file which will
    #show all the dependencies that have been installed (dependencies required for the project).
    # - Use "pip install -r requirements.txt" to install all the dependencies listed in a requirements.txt file.
    # - The gitignore file contains files/folders which you don't want to upload to GitHub.


#5. Flask API Example: Hello Rest API
    # Create a file called app.py which will contain the code below
    # Run the app by using the bash command "python app.py". NOte that you need
    #to be in the app's directory in the terminal in order for it to work.
    # Now visit http://localhost:5000 in your browser. You’ll see “Hello, REST API!”

 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, REST API!'

if __name__ == '__main__':
    app.run(debug=True)
