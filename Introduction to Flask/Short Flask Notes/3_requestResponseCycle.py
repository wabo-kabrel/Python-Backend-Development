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


#C. Request Dispatching