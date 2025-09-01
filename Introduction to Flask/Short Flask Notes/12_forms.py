# Flask Web Forms

# Flask provides a way to handle web forms easily using the Flask-WTF extension,
# which integrates WTForms with Flask.
# WTForms is a flexible forms validation and rendering library for Python web development.

#1. The Problem with Raw Forms
# In plain Flask, you can use request.form to grab form data:
'''
from flask import request

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
'''
    # The approach above works but:
        # - You need to hand-write all HTML form tags.
        # - You need to manually validate inputs (empty fields, bad email, etc.).
        # - You must add CSRF protection yourself.


#2. Flask-WTF
# - Flask-WTF is a Flask extension that wraps WTForms, making forms much easier:
    # - Auto-generates HTML fields.
    # - Provides validators (like "required", "email", "length").
    # - Protects forms against CSRF attacks automatically.
# - To use Flask-WTF, install it via pip:
'''pip install flask-wtf
'''

#3. CSRF Protection
# - A CSRF attack = tricking a logged-in user into submitting a form they didn’t intend.
# - Flask-WTF fixes this by embedding a hidden token inside every form.
# - Flask needs a secret key to generate this token.
'''
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a-very-secret-key'  # 🔑 keep this hidden in real apps!
'''

#4 Defining Forms with Classes
# Each form = a Python class that inherits from FlaskForm (modern import).
# Example: a simple "Name Form".
'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")
'''
# - StringField → <input type="text">
# - SubmitField → <input type="submit">
# - DataRequired() → validator: field must not be empty

#5. Rendering Forms in Templates
# In your Flask route, create an instance of the form and pass it to a Jinja 2 template:
'''
from flask import render_template

@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    return render_template("index.html", form=form)
'''

# Minimal template (templates/index.html):
'''
<form method="POST">
    {{ form.hidden_tag() }} <!-- 🔑 CSRF token -->
    {{ form.name.label }} {{ form.name() }}
    {{ form.submit() }}
</form>
'''
# Flask-WTF makes fields callable: form.name() generates HTML <input>.


#6. Handling Form Submission
# In your route, check if the form was submitted and validated:
'''
@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    name = None
    if form.validate_on_submit():
        name = form.name.data   # get input value
        form.name.data = ""     # clear field
    return render_template("index.html", form=form, name=name)
'''


#7. Using Sessions + Redirect (Best Practice)
# - Problem: if you refresh after POST, browser may re-submit the form.
# - Fix: use Post/Redirect/Get pattern:
'''
from flask import session, redirect, url_for

@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))  # redirect after POST
    return render_template("index.html", form=form, name=session.get('name'))
'''
# - session = a dictionary stored in a secure cookie (signed with SECRET_KEY)


#8. Flask Messages
# Flash gives feedback to the user (e.g., success, error or warning):
'''
from flask import flash

if form.validate_on_submit():
    old_name = session.get('name')
    if old_name and old_name != form.name.data:
        flash("Looks like you changed your name!")
    session['name'] = form.name.data
    return redirect(url_for("index"))
'''
# Display in template (base.html):
'''
{% for message in get_flashed_messages() %}
  <div class="alert alert-warning">{{ message }}</div>
{% endfor %}
'''


#9. Validators you can use 
# - DataRequired() → must not be empty
# - Email() → must be valid email
# - Length(min=3, max=50) → string length check
# - NumberRange(min=18, max=99) → numbers only in range
# - EqualTo('password2') → confirm password
# - URL() → must be a valid URL

# Connect them like this:
'''
email = StringField("Email", validators=[DataRequired(), Email()])
'''

#10. Rendering with bootstrap
# If you install Flask-Bootstrap, you can render the whole form prettily:
'''
{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}
'''
# That’s one line instead of writing all fields manually.