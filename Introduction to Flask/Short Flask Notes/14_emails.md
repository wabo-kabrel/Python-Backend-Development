# 📬 Emails in Flask (with Flask-Mail)
## 1. Why Email Matters in Web Apps
- Many apps need to **notify users**:
  - Password resets
  - Account confirmation
  - Alerts/notifications
- The usual tool → **Email**
 
Flask doesn’t have built-in email, but Python’s `smtplib` can send emails.
However, it’s **low-level**. That’s why we use **Flask-Mail**.


## 2. Flask-Mail: The Email Extension
- **Flask-Mail** wraps Python's `smtplib`.
- It integrates with Flask to make sending email **simple** and **flexible**.

**Install:**
```bash
pip install flask-mail
```


## 3. How Email Sending Works
1. Your app → Flask-Mail.
2. Flask-Mail → SMTP server (e.g., Gmail, Outlook, SendGrid).
3. SMTP server → delivers email to recipients.


## 4. Flask-Mail Configuration Keys
These config values go into the `app.config`:
| Key             | Default     | Description              |
| --------------- | ----------- | ------------------------ |
| `MAIL_SERVER`   | `localhost` | Email server hostname/IP |
| `MAIL_PORT`     | `25`        | Port number              |
| `MAIL_USE_TLS`  | `False`     | Enable TLS security      |
| `MAIL_USE_SSL`  | `False`     | Enable SSL security      |
| `MAIL_USERNAME` | `None`      | Username (if required)   |
| `MAIL_PASSWORD` | `None`      | Password (if required)   |


## 5. Example: Configure Gmail
```python
import os
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)
```
⚠️ **Security Tip**: Never hardcode credentials. Use **environment variables**:
```bash
# Linux/Mac
export MAIL_USERNAME="your@gmail.com"
export MAIL_PASSWORD="yourpassword"

# Windows (cmd)
set MAIL_USERNAME=your@gmail.com
set MAIL_PASSWORD=yourpassword
```


## 6. Sending a Simple Email
```python
from flask_mail import Message

@app.route("/send")
def send_test():
    msg = Message(
        subject="Hello from Flask",
        sender="your@gmail.com",
        recipients=["friend@example.com"]
    )
    msg.body = "This is a plain text email."
    msg.html = "<b>This is an HTML email.</b>"

    with app.app_context():  # Flask-Mail requires an app context
        mail.send(msg)

    return "Email sent!"
```
✅ Notes:
- `msg.body` → plain text
- `msg.html` → rich HTML
- Always run `mail.send()` inside `app.app_context()`.


## 7. Abstracting Email into a Helper Function
Instead of writing `Message` each time, create a **utility function**:
```python
from flask import render_template

app.config['MAIL_SUBJECT_PREFIX'] = '[MyApp]'
app.config['MAIL_SENDER'] = 'MyApp Admin <your@gmail.com>'

def send_email(to, subject, template, **kwargs):
    msg = Message(
        subject=app.config['MAIL_SUBJECT_PREFIX'] + subject,
        sender=app.config['MAIL_SENDER'],
        recipients=[to]
    )
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
```
- `render_template` lets you design emails with Jinja2 templates.
- Store templates in `templates/mail/`:
  - `mail/welcome.txt` (plain text)
  - `mail/welcome.html` (HTML)


## 8. Example: Sending When User Registers
```python
@app.route("/", methods=["POST"])
def index():
    name = request.form.get("name")
    if name:
        if app.config['ADMIN_EMAIL']:
            send_email(
                app.config['ADMIN_EMAIL'],
                "New User Registration",
                "mail/new_user",
                user=name
            )
    return "Form submitted!"
```
Environment variable:
```bash
export ADMIN_EMAIL=your@gmail.com
```


## 9. Problem: Email Sending Blocks Request
- `mail.send(msg)` is **slow** (waits for SMTP server).
- Browser feels “frozen” for a few seconds.
👉 Solution: **Asynchronous Email**


## 10. Sending Async Emails (Threads)
```python
from threading import Thread

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    msg = Message(
        subject=app.config['MAIL_SUBJECT_PREFIX'] + subject,
        sender=app.config['MAIL_SENDER'],
        recipients=[to]
    )
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)

    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
```
- Starts a new **thread** → app stays responsive.
- `app.app_context()` ensures Flask context exists in new thread.


## 11. Production-Ready Email (Beyond Flask-Mail)
For `big apps` or high email volume:
- Use a **task queue** (Celery, RQ) instead of raw threads.
- Use **email services** (SendGrid, Amazon SES, Mailgun).