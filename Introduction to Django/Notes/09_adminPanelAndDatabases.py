# Django Admin Panel and Basic Database Operations

#1. What is the Django Admin
# - The Django Admin is an auto-generated, password-protected web interface for 
#   managing your site's data.
# - With zero code, you can:
    # - Add, edit, and delete records in your database.
    # - Manage users and permissions.
    # - Inspect and test models.


#2. Enabling and Accessing the Admin Panel
# - Ensure "django.contrib.admin" is included in INSTALLED_APPS in settings.py (already is by default).
# - Ensure "django.contrib.auth" and "django.contrib.contenttypes" are also present (they handle users
#   and permissions).
# - Run your server:
'''
python manage.py runserver
'''
# - Visit http://127.0.0.1:8000/admin/
# - Login with your superuser account (created in lesson 8).


#3. Registering Models in Admin
# - Earlier in lesson 8, we already registered the Contact model in home/admin.py to make it manageable via the admin panel.
# - Now let's a Task model to manage tasks.
# - In home/admin.py;
'''
from django.contrib import admin
from .models import Contact, Task

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'created_at')
    list_filter = ('is_completed',)
    search_fields = ('title',)
'''
# Enhancements:
# - list_display: columns shown in the admin list view
# - search_fields: allows searching in the admin
# - list_filter: adds a sidebar filter (e.g. by completion status)


#4. Performing CRUD Operations
# - Create: Click “Add Task” → fill form → Save.
# - Read: Tasks list view shows records.
# - Update: Click on a Task → edit → Save.
# - Delete: Select and delete


#5. Performing CRUD in Django Shell
# - Open Python shell `python manage.py shell`
# - Create:
'''
from home.models import Task
task = Task.objects.create(title="Learn Django Models", is_completed=False)
'''
# - Read:
'''
Task.objects.all()                  # All tasks
Task.objects.filter(is_completed=False)   # Pending tasks
'''
# - Update:
'''
task = Task.objects.get(id=1)
task.is_completed = True
task.save()
'''
# - Delete:
'''
task.delete()
'''


#6. Best Practices for Admin
# - Use list_display for better visibility.
# - Add search_fields for easy searching.
# - Add list_filter for filtering large datasets.
# - Customize forms if you need complex output.
# - Restrict access using Django's permissions system. Not everyone should be a superuser.