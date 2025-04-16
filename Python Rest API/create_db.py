from api import app, db

with app.app_context():
    db.create_all()
    

# - The code above is used to create the database tables from
#the SQLAlchemy models.

# - "from api import app, db" imports the app and db objects from the api module.
# - app is the Flask object and db is the SQLAlchemy instance.

# - app.app_context() creates a context for the application. Flask uses application contexts
#to manage variables like configuration, database connections, etc.
# - Some actions (like db.create_all()) need access to the app’s context to know what app they're working with.
# - This app.app_context() creates a temporary context so database operations can run outside the web server
#(like in scripts or shells).

# - db.create_all() creates all the tables defined in the SQLAlchemy models (UserModel in this case).
# - It checks if tables already exist; if they don’t, it creates them.
# - It does not drop or update existing tables — it only creates what’s missing.

# - Now, run the script with the bash command "python create_db.py" in order to create the database.
# - The database will be created in the file called database.db and stored in a folder called instance.
