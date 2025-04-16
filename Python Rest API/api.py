from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# The route is used to request data from the server.
# The data is requested using a URL.
# The response is sent back to the client (browser).

@app.route('/')     # A slash / comes after the domain 
def home():
    return '<h1>Flask Rest API</h1>'

if __name__ == '__main__':
    app.run(debug=True)
    

# - app.run() launches the built-in Flask server so your app can start receiving
#requests. By default, it runs on http://127.0.0.1:5000/.
# - Setting debug = True gives you auto-reload such that you don't have to restart the server
#after making changes to your code. And it also provides you with an interactive debugger. That is,
#Flask shows you an interactive error page in the browser if your app crashes or throws an error.
# - Never use debug = True in production, because it exposes internal info to users and it can be 
#a security risk. Only use it during development, as it helps you build faster and debug easier.