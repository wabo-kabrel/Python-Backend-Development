#1. What is an API?
'''API stands for Application Programming Interface. It is like a waiter in a restaurant. You
(the client) ask for food (data), the waiter (API) takes your order to the kitchen (server), and
brings you the food (response).'''
# APIs allow two applications to talk to each other. E.g. Your phone app sends a request to a weather server.


#2. What is a REST API?
    # REST = Representational State Transfer.
    # REST is a style (not a technology) used to design networked applications.

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


#4. Installing Flask
    # Use the bash command: pip install flask


#5. Flask API Example: Hello World API
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
