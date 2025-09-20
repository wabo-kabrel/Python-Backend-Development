#1. Static vs Dynamic URLs
# - Static URL: /about/, /contact/, → same page every time.
# - Dynamic URL: /task/1/, /task/2/, → different content based on the parameter.

# - Example:
    # - Blog: /post/42/ → fetches blog post with ID 42.
    # - E-commerce: /product/iphone-15/ → fetches product details.


#2. Adding a Dynamic URL Pattern 
# - We'll add a detail page for Task.
# - In home/urls.py, add:
'''
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("task/<int:id>/", views.task_detail, name="task_detail"),
]
'''
# - <int:id> means this URL will capture a number (e.g. /task/5/) and pass it as an argument id to the view.


#3. Creating the Task Detail View
# - In home/views.py, add:
'''
from django.shortcuts import render, get_object_or_404
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, "home/index.html", {"tasks": tasks})

def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, "home/task_detail.html", {"task": task})
'''

# - get_object_or_404 → fetches the object or returns a 404 error if not found.
#   (Without it, you'd get a crash if the ID doesn't exist.)


#4. Creating the Task Detail Template
# - In home/templates/home/task_detail.html;
'''
<!DOCTYPE html>
<html>
<head>
    <title>{{ task.title }}</title>
</head>
<body>
    <h2>{{ task.title }}</h2>
    <p>Status: {% if task.is_completed %} ✅ Completed {% else %} ⏳ Pending {% endif %}</p>
    <p>Created at: {{ task.created_at }}</p>
    <a href="{% url 'home' %}">Back to Home</a>
</body>
</html>
'''


#5. Link Tasks to Their Detail Pages
# - Modify your index.html to make each task clickable:
# - In home/templates/home/index.html;
'''
<h2>Tasks</h2>
<ul>
    {% for task in tasks %}
        <li>
            <a href="{% url 'task_detail' task.id %}">
                {{ task.title }}
            </a>
        </li>
    {% empty %}
        <li>No tasks available.</li>
    {% endfor %}
</ul>
'''


#6. Testing Dynamic Routing
# - Run the server: python manage.py runserver
# - Visit: http://127.0.0.1:8000/
# - Click a task → you should land on its detail page (/task/1/, /task/2/, etc.).
# - If you enter an invalid ID (/task/999/), you’ll see a 404 page.


#7. Path Converters in Django 
# - You can capture different types of URL parameters:
#   | Converter     | Example URL                  | Value in View     |
#   | ------------- | ---------------------------- | ----------------- |
#   | `<int:id>`    | `/task/5/`                   | `5` (integer)     |
#   | `<str:name>`  | `/user/kabrel/`              | `"kabrel"`        |
#   | `<slug:slug>` | `/blog/my-first-post/`       | `"my-first-post"` |
#   | `<uuid:id>`   | `/order/550e8400-e29b-41d4/` | UUID object       |


