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