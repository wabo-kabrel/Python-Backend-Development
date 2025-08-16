#1. Why Custom Error Pages?
# - By default, Flask sends you a plain, ugly HTML error page of:
    # - You go to a route that doesn't exist (404 Not Found)
    # - Your app crashes unexpectedly (500 Internal Server Error)
# - Problem:
    # These default pages look nothing like the rest of your site — no navigation
    # bar, no styling, no brand identity.
# - Solution:
    # We override these defaults with custom handlers that:
    # - Use templates (so they look like the rest of your site)
    # - Can use Bootstrap or your own CSS for styling
    # - Can be reused for multiple error types


#2. How to Create Custom Error Pages
# - Flask lets you "catch" certain HTTP errors and run your own function for them
#   using @app.errorhandler().
# - Example:
'''
from flask import render_template

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
'''