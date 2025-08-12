# Command Line Options with Flask

#1. The Problem
# - Normally, if you want to configure how Flask runs(host, port, debug mode, etc),
#   you pass arguments inside your code like:
'''
app.run(debug=True, port=5001)
'''
# But this means you have to edit the code every time you want to change something, which is 
# not ideal. Command line options lets us pass these options directly from the command line
# instead.


#2. The Solution — Flask-Script
# - Flask-Script is a Flask extension that:
    # - Adds a command-line parser to your app.
    # - Lets you run predefined commands like:
        # - runserver → start the Flask server
        # - shell → open a Python shell inside Flask’s app context
    # - Lets you create your own commands.


#3. Installing Flask-Script
# - Install FLask-Script with the bash command, `pip install flask-script`


#4. Setting It Up
# - Let's say you have a simple Flask app in hello.py:
#i. Without Flask-Script:
'''
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
'''

#ii. With Flask-Script:
'''
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)  # attach Manager to the app

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

if __name__ == "__main__":
    manager.run()  # run Manager instead of app.run()
'''


#5 What Changes?
# - When you run `python hello.py`, you'll now see:
'''
usage: hello.py [-h] {shell,runserver} ...
positional arguments:
  {shell,runserver}
    shell       Runs a Python shell inside Flask application context.
    runserver   Runs the Flask development server i.e. app.run()

optional arguments:
  -h, --help    Show help message and exit
'''


#6. Default Commands
#i. runserver
# - Starts the flask development server: `python hello.py runserver`
# - It is equivalent to '''app.run(debug=True)''' but with extra options.

#ii. shell
# - Opens a Python shell inside your Flask app context: `python hello.py shell`
# - It is useful for:
    # - Running database queries
    # - Testing functions
    # - Debugging


#7. Extra Options for runserver 
# - Run `python hello.py runserver --help` to see the extra options below:
'''
usage: hello.py runserver [-h] [-t HOST] [-p PORT] [--threaded]
                           [--processes PROCESSES] [--passthrough-errors]
                           [-d] [-r]

optional arguments:
  -t HOST, --host HOST     Host interface (default: 127.0.0.1)
  -p PORT, --port PORT     Port number (default: 5000)
  --threaded               Handle requests in separate threads
  --processes PROCESSES    Number of worker processes
  --passthrough-errors     Don’t trap exceptions
  -d, --no-debug           Disable debug mode
  -r, --no-reload          Disable auto-reloader
'''


#8. Most Useful Options
#i Change Host
# - Run `python hello.py runserver --host 0.0.0.0`
# - Makes the app accessible from any computer in your network.
# - Default is 127.0.0.1 (localhost only).

#ii. Change Port 
# - Run `python hello.py runserver --port 8080`
# - Runs the server on port 8080 instead of 5000.

#iii. Threaded Mode
# - Run `python hello.py runserver --threaded`
# - Handles multiple requests at the same time using threads.

#iv. Multiple Processes
# - Run `python hello.py runserver --processes 4`
# - Runs with multiple worker processes.

#v. Disable Debug Mode
# - Run `python hello.py runserver --no-debug`


#9 Real-World Example
# - Let’s say you want to start your app for other devices on your Wi-Fi to access
#   it, on port 9000, and enable threading:
    # - Run `python hello.py runserver --host 0.0.0.0 --port 9000 --threaded`
    # - If your computer’s IP is 192.168.1.5, others can visit http://192.168.1.5:9000


#10. Summary Table

# | Command                     | Purpose                               |
# | --------------------------- | ------------------------------------- |
# | `python hello.py runserver` | Start Flask server                    |
# | `--host 0.0.0.0`            | Allow connections from other devices  |
# | `--port 8080`               | Change port                           |
# | `--threaded`                | Handle requests in multiple threads   |
# | `--processes N`             | Handle requests in multiple processes |
# | `python hello.py shell`     | Open Python shell in Flask context    |
