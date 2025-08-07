
from flask import (Flask, render_template, abort, url_for, json, jsonify)
# - Flask will provide the application instance
# - render_template will allow us to render HTML templates
# - abort will allow us to return error codes
# - url_for will allow us to generate URLs for the application
# - json will allow us to parse JSON data
# - jsonify will encode Python dictionaries into JSON strings

# Creating a Flask application instance
app =Flask(__name__, template_folder='.') # template_folder='.' means the templates are 
                                          # in the current directory
with open('file.json', 'r') as f:
    data = f.read()

@app.route('/')
def index():
    return render_template('index.html', jsonfile = json.dumps(data))

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')