from flask import Flask

app = Flask(__name__)

# The route is used to request data from the server.
# The data is requested using a URL.
# The response is sent back to the client (browser).

@app.route('/')     # A slash / comes after the domain 
def home():
    return '<h1>Flask Rest API</h1>'

if __name__ == '__main__':
    app.run(debug=True)