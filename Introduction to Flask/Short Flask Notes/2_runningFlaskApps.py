# There are two ways to run a Flask app:
#1. Exporting the Flask app variable:
# - Make sure you have Flask installed in your virtual environment, and the
#   the virtual environment is activated.
# - In your terminal, set the `FLASK_APP` environment variable to the name
#   of your application file (without the `.py` extension).
# - For example, if your file is named `app.py`, you would run:
#   ``` set FLASK_APP=app ``` (on Windows)
#  ``` export FLASK_APP=app ``` (on macOS/Linux)
# - Then, run the Flask application using the command: `flask run`
# - You should see " Running on http://127.0.0.1:5000"


#2. Running Programmatically
# - The flask development server can be run programmatically by invoking 
#   the app.run() method, where 'app' is the instance of the Flask class.
# - This method was used in older versions of Flask which didn't support the
#   `flask run` command.
# - No need to focus on this since we can always use the `flask run` command
#   as shown in #1.


#   Debugging in Flask
# - Flask applications can optionally be executed in debug mode.
# - When debug mode is enabled, the server will automatically reload
#   when code changes are detected, eliminating the need to restart the server manually.
# - We can enable this according to the way we choose to run our application.

#i. Considering that we want to use the `flask run` command, we can enable 
#   debug mode by passing ` set FLASK_DEBUG=1` (for Windows) or `export FLASK_DEBUG=1` (for macOS/Linux)
#   in the terminal.
# - After enabling debug mode, we now use `flask run --debug` instead of `flask run` in
#   the terminal to run the application.
# - That is:
        # First command: `FLASK_DEBUG=1`
        # Second command: `flask run --debug`

#ii. If running our application programmatically, we need to pass "app.run(debug=True)"
#    after the conditional statement "if __name__ == '__main__'" in your code.
# - That is:
'''
if __name__ == '__main__':
    app.run(debug=True)'
'''
# - We now run the application using the command: `python app.py` in the terminal


#   Disabling Debug Mode
# - Debug mode can be disabled by passing ` set FLASK_DEBUG=0` (for Windows) or `export FLASK_DEBUG=0
#   (for macOS/Linux), when running the `flask run` command.
# - Programmatically, we simply pass "app.run(debug=False)".


# Flask Command-Line Options
# - The flask command supports a number of options.
# - To see the available commands and options run `flask --help` or just `flask`.
