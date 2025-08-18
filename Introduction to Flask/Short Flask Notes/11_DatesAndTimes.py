# The Problem with Dates & Times in Web Apps
# - Users can be all over the world in different time zones.
# - If your server shows UTC time (universal time), users in Cameroon,
#   USA, India, etc., won’t see the correct local time.
# - Example: Your server logs 2025-08-17 06:30:00 UTC
    # - A user in New York expects 2:30 AM
    # - A user in Cameroon expects 7:30 AM
    # - A user in Tokyo expects 3:30 PM
# - To fix this, we let the server store everything in UTC (clean & consistent), 
#   but let the browser display times in local time.


# 🔹 The Tool: Flask-Moment
# - Moment.js → A JavaScript library that formats dates & times on the browser side.
# - Flask-Moment → A Flask extension that integrates moment.js into Jinja2 templates.

#  📦 Install: `pip install flask-moment`

# 🔹 How to Use Flask-Moment
#1. Initialize it
'''
`python`

from flask import Flask, render_template
from flask_moment import Moment   # modern import (not flask.ext)

app = Flask(__name__)
moment = Moment(app)
'''

#2. Include Moment.js in your Template
# Flask-Moment can automatically add moment.js from a CDN.
'''
{% block scripts %}
  {{ super() }}
  {{ moment.include_moment() }}   <!-- injects moment.js -->
{% endblock %}
'''
# This makes moment available in templates.

#3. Pass UTC datetime from Flask to Template
'''
from datetime import datetime

@app.route('/')
def index():
    return render_template("index.html", current_time=datetime.utcnow())
'''
# Notice: We use datetime.utcnow() (not local time).
# Flask-Moment will take care of converting it for the user.


#4. Display Dates in Templates
'''
<p>The local date and time is {{ moment(current_time).format('LLL') }}.</p>
<p>That was {{ moment(current_time).fromNow(refresh=True) }}</p>
'''
# - format('LLL') → Formats according to the user’s computer locale & timezone.
    # - L → short date
    # - LLL → date + time (medium verbosity)
    # - LLLL → full verbose format
# - fromNow(refresh=True) → Shows relative time (e.g., "a few seconds ago", "2 minutes ago")
#   and updates dynamically


# 🔹 Extra Features of Flask-Moment
# - .fromTime(datetime) → relative to a specific time
# - .calendar() → shows “Today at 3:00 PM” style text
# - .unix() → displays Unix timestamps
# - .lang('es') → change language (es = Spanish, fr = French, etc.)
# - Example:
'''
{{ moment.lang('fr') }}
<p>Il est {{ moment(current_time).format('LLLL') }}</p>
'''

# ✅ Why Use Flask-Moment?
# - Keeps server logic simple → Always UTC.
# - Browser handles timezone + locale formatting.
# - Better user experience (everyone sees their local time).


# 🔹 Example in Action:
'''
from flask import Flask, render_template
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
moment = Moment(app)

@app.route('/')
def index():
    return render_template("index.html", current_time=datetime.utcnow())

if __name__ == '__main__':
    app.run(debug=True)
'''
# index.html:
'''
<!DOCTYPE html>
<html>
<head>
    <title>Flask-Moment Example</title>
</head>
<body>
    <p>The local date and time is {{ moment(current_time).format('LLL') }}.</p>
    <p>That was {{ moment(current_time).fromNow(refresh=True) }}</p>
    {% block scripts %}
      {{ moment.include_moment() }}
    {% endblock %}
</body>
</html>
'''