#       Request - Response Cycle in Flask

#A. Overview the Flask Request-Response Cycle
# - When a user makes a request to your Flask application, here's what happens
#   step by step:
'''
User Browser → Web Server → WSGI → Flask App → Route Matching → View Function → Response → WSGI → Web Server → User Browser
'''
#1. User initiates request: Browser sends HTTP request (GET, POST, etc.)
#2. Web server receives: Apache/Nginx receives the request
#3. WSGI interface: Web Server Gateway Interface passes request to Flask
#4. Flask receives: Flask app object gets the request
#5. Context creation: Flask creates application and request contexts
#6. URL routing: Flask matches the URL to a view function
#7. View execution: Your view function runs and processes the request
#8. Response creation: Flask builds the HTTP response
#9. Context cleanup: Flask tears down contexts
#10. Response delivery: Response travels back through WSGI to user
     
#    Role of WSGI
# - WSGI (Web Server Gateway Interface) is the bridge between your Flask app
#   and the web server. It's a specification that defines how web servers
#   communicate with Python web applications.
#---------------------------------------------------------------------------------------------------------


#B. Application Context and Request Context
# - A context allows Flask to track which application or request is currently active.

#1. Application Context
# - Created: when you push it with app.app_context() or during a request.
# - Objects available: current_app, g
          # - current_app is an instance of the active Flask application.
          # - g is an object that the application can use for temporary storage during
          #   the handling of a request.
# - Use case: background tasks, CLI commands, database init

#2. Request Context
# - Created: automatically on each request.
# - Objects available: request, session, g
            # - request contains data about the current HTTP request (form data, headers, etc.).
            # - session is used to store user-specific data across requests.
            # - g is also available here for temporary storage.
# - Use case: route handlers, request data processing

'''
from flask import Flask, current_app, request, g

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

@app.route('/context-demo')
def context_demo():
    # current_app - points to the Flask application instance
    app_name = current_app.name
    
    # request - contains current request data
    method = request.method
    url = request.url
    
    # g - temporary storage for the current request
    g.user_id = 123  # Store data for this request only
    
    return f"""
    App Name: {app_name}
    Method: {method}
    URL: {url}
    Stored in g: {g.user_id}
'''

# Example: Using contexts outside of request
'''def test_contexts():
    # This will fail - no application context
    try:
        print(current_app.name)
    except RuntimeError as e:
        print(f"Error: {e}")
    
    # Manually create application context
    with app.app_context():
        print(f"App name: {current_app.name}")
        
        # This will still fail - no request context
        try:
            print(request.method)
        except RuntimeError as e:
            print(f"Error: {e}")
        
        # Create request context too
        with app.test_request_context('/test'):
            print(f"Request method: {request.method}")
            print(f"Request path: {request.path}")

if __name__ == '__main__':
    # Run context test
    test_contexts()
    app.run(debug=True)
'''
#---------------------------------------------------------------------------------------------------------


#C. Request Dispatching
#                How Flask Maps URLs to View Functions
#   Flask uses Werkzeug's routing system to match URLs to view functions.
#   Here's how it works:
#1. URL Map Creation: Flask builds a URL map from your @app.route() decorators
#2. Request Analysis: When a request comes in, Flask analyzes the URL and HTTP method
#3. Route Matching: Flask searches the URL map for a matching route
#4. View Function Execution: If found, Flask calls the corresponding view function
#5. Error Handling: If no match, Flask returns 404 (Not Found) or 405 (Method Not Allowed)

#   URL Converters
#   Flask supports several built-in URL converters:
# - string (default): Accepts any text without a slash
# - int: Accepts positive integers
# - float: Accepts positive floating point values
# - path: Like string but accepts slashes
# - uuid: Accepts UUID strings
#---------------------------------------------------------------------------------------------------------

#D. Request Object
# - The request object contains all the data from the current HTTP request. It's
#   automatically available in your view functions.

# - Request methods
    # - Request methods indicate the type of action being requested. They include:
        # - get_data: Returns the raw data of the request body.
        # - get_json: Returns a Python dictionary with parse JSON data from the request body.
        # - is_secure: Returns True if the request is made over HTTPS.

# - Important variables through the request object:
    # - endpoint: The name of the flask endpoint that's handling the request.
    # - method: Gives the HTTP request such as GET or POST  
    # - host: The host defined in the request, including the port number if given by the client.
    # - url: The complete URL requested by the client.
    # - environ: The raw whiskey environment dictionary for the request.  

# - Request Hooks
# At times, it is useful to execute some code before and after each request is is proceeded.
# E.g. At the start of every request, it may be necessary to create a database connection or 
# authenticate the user making the request. Instead of duplicating the code that performs these
# actions in every View function, Flask gives you the option to register common functions to be 
# invoked before or after a request is dispatched.
# The most common use case is to close database connections after a request is processed.
# Request hooks are implemented with decorators, and these are the 04 hooks supported by Flask:
        # - before_request: Registers the function to be executed before each request.
        # - before_first_request: Registers a function to run only before the first request is handled.
            #   This can be a convenient way to handle server initialization tasks.
        # - after_request: Registers a function to run after each request, but only if no unhandled
            # exceptions occurred.   
        # - teardown_request: Registers a function to run after every request, even when unhandled
            # exceptions occur.  

#   Key Request Object Properties
# - request.method: HTTP method (GET, POST, etc.)
# - request.form: Form data from POST requests
# - request.args: Query string parameters
# - request.json: JSON payload (if Content-Type is application/json)
# - request.files: Uploaded files
# - request.headers: Request headers
# - request.cookies: Cookies sent by client
# - request.path: The path of the requested URL
#---------------------------------------------------------------------------------------------------------

#E. The Response Object
# - Flask automatically converts your return values into Response objects, 
#   but you can also create them manually for more control.

#   Ways to Return Responses in Flask
#1. String: Flask automatically creates a Response object
#2. Dictionary: Automatically converted to JSON
#3. Tuple: (body, status_code) or (body, status_code, headers)
#4. Response object: Full control over the response
#5. make_response(): Helper function to create Response objects