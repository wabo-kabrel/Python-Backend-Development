#1. What is an API?
# - API (Application Programming Interface): A way for apps to talk to each other.
# - REST API: Uses HTTP methods (GET, POST, PUT, DELETE) to interact with data.
    # - GET /tasks/ → list all tasks
    # - POST /tasks/ → create a new task
    # - GET /tasks/1/ → get details of task with id 1
    # - PUT /tasks/1/ → update task with id 1
    # - DELETE /tasks/1/ → delete task with id 1
# - REST APIs return data in JSON format so frontend/mobile apps can use it.


#2. Installing Django REST Framework
# - Install via pip: pip install djangorestframework
# - Add 'rest_framework' to INSTALLED_APPS in settings.py:
'''
INSTALLED_APPS = [
    ...
    'rest_framework',
    'home',   # our app
]
'''


#3. Creating a Serializer
# - Serializers convert Django models to JSON and vice versa.
# - In home/serializers.py:
'''
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'is_completed', 'created_at']
'''


#4. Creating API views 
#i. Using DRF's class-based views (APIView):
# - In home/views.py:
'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404

class TaskListCreate(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, id):
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        task = get_object_or_404(Task, id=id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

#ii. Using DRF's generic views:
# - In home/views.py (short version):
'''
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
'''
# Same functionality with less code.


#5. Defining API URLs
# - In home/urls.py:
'''
from django.urls import path
from .views import TaskListCreate, TaskDetail

urlpatterns = [
    path("api/tasks/", TaskListCreate.as_view(), name="task_list"),
    path("api/tasks/<int:id>/", TaskDetail.as_view(), name="task_detail"),
]
'''


#6. Testing the API
# - Run the server: python manage.py runserver
# - Visit http://127.0.0.1:8000/api/tasks/
    # - If you GET → you’ll see a JSON list of tasks.
    # - If you POST (via Postman, curl, or DRF’s built-in form) → a new task is created.
    # - Visit http://127.0.0.1:8000/api/tasks/1/ → see task details.