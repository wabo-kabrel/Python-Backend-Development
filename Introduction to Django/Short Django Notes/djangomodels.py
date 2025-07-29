#1. Django Models
#i. What is a Model in Django?
# - A model is a Python class that defines the structure of your
#   database tables. Django automatically maps these models to actual
#   tables in the database using the Object-Relational Mapper (ORM).


#ii. What is an ORM?
# - An Object-Relational Mapper (ORM) is a tool that allows you to
#   interact with a database using Python objects instead of raw SQL queries. 
#   Django provides a built-in ORM that is based on the popular SQLAlchemy library. 

#iii. What is a QuerySet?
# - A QuerySet is a collection of objects that are retrieved from a
#   database based on a set of conditions. QuerySets are used to perform
#   complex queries and operations on database data.


#2. Defining a Simple Model
# - Let’s create a Contact model to store contact form submissions.
#i - Open home/models.py and add:
'''
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
'''
# - Model Fields:
    # - CharField: For short text (e.g. name)
    # - EmailField: For emails (with validation)
    # - TextField: For long text (e.g. messages)
    # - DateTimeField: Stores timestamps (auto_now_add=True saves when created)


#3. Activating the Model
#i. Make Migrations
# - Run `python manage.py makemigrations`.
# - This creates a migration file in home/migrations/ that
#   tells Django how to build the table.

#ii. Apply the Migrations
# - Run `python manage.py migrate`.
# - Now the table is created in your database (by default, SQLite).


#4. Registering the Model in Admin
# - Open home/admin.py:
'''
from django.contrib import admin
from .models import Contact

admin.site.register(Contact)
'''


#5. Create Superuser (if you haven't)
# - Run `python manage.py createsuperuser`
# - Enter:
    # - Username
    # - Email
    # - Password


#6. Accessing the Django Admin Panel
# - Run the server and visit: http://127.0.0.1:8000/admin/
# - Log in using the superuser credentials.
# - You'll see the Contacts listed there, Django created this interface automatically.


#  Behind the Scenes (How Django ORM Works)
#   ----------------------------------------------------------------------------------------- 
#   | You write this in Python                | Django runs this SQL                        |
#   |---------------------------------------- | ------------------------------------------- |
#   | `Contact.objects.all()`                 | `SELECT * FROM contact`                     |
#   | `Contact.objects.create(...)`           | `INSERT INTO contact (...)`                 |
#   | `Contact.objects.filter(name="Kabrel")` | `SELECT * FROM contact WHERE name='Kabrel'` |
#   -----------------------------------------------------------------------------------------


# Optional Step: Saving a Model in Shell
# - Run `python manage.py shell`
'''
from home.models import Contact
contact = Contact(name="Kabrel", email="kabrel@mail.com", message="Django is great!")
contact.save()

Contact.objects.all()
'''


# Summary:
# - Models define your data schema using Python classes.
# - Django ORM handles all database operations for you.
# - Migrations are how you create or update your database schema.
# - Django Admin gives you an instant backend interface.
