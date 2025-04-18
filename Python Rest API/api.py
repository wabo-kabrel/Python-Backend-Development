# Import necessary libraries
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort


# Initialize Flask app
app = Flask(__name__) 

# Set the database URI — using SQLite database called 'database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Initialize SQLAlchemy for database handling
db = SQLAlchemy(app)                # SQLAlchemy(app) connects the app to the database.

# Initialize Flask-RESTful for creating REST API endpoints
api = Api(app)


class UserModel(db.Model):              # Defines a model ( a table in the database called UserModel)
    # Unique ID for each user
    id = db.Column(db.Integer, primary_key=True)
    
    # User's name (a column in the table) — must be unique and not null
    name = db.Column(db.String(80), unique=True, nullable=False)
    
    # User's email — must be unique and not null
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):         # returns a string representation of the object in the database
        # For debugging and logging purposes
        return f"User(name = {self.name}, email = {self.email})"


# Create a parser for incoming request data
user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help="Name cannot be blank")
user_args.add_argument('email', type=str, required=True, help="Email cannot be blank")


# Define how the data will be serialized into JSON
userFields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
}


class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        # Fetch all users from the database
        users = UserModel.query.all() 
        return users 


    @marshal_with(userFields)
    def post(self):
        # Parse and validate incoming JSON
        args = user_args.parse_args()
        
        # Create a new user
        user = UserModel(name=args["name"], email=args["email"])
        db.session.add(user) 
        db.session.commit()

        # Return updated user list and HTTP 201 status
        users = UserModel.query.all()
        return users, 201


class User(Resource):
    @marshal_with(userFields)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first() 
        if not user: 
            abort(404, message="User not found")
        return user 


    @marshal_with(userFields)
    def patch(self, id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=id).first() 
        if not user: 
            abort(404, message="User not found")

        # Update the user info
        user.name = args["name"]
        user.email = args["email"]
        db.session.commit()
        return user 


    @marshal_with(userFields)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first() 
        if not user: 
            abort(404, message="User not found")

        # Delete the user
        db.session.delete(user)
        db.session.commit()

        # Return updated list of users
        users = UserModel.query.all()
        return users


api.add_resource(Users, '/api/users/')          # For all users
api.add_resource(User, '/api/users/<int:id>')   # For individual user by ID


# The route is used to request data from the server.
# The data is requested using a URL.
# The response is sent back to the client (browser).
@app.route('/')         # A slash / comes after the domain
def home():
    return '<h1>Flask REST API</h1>'

if __name__ == '__main__':
    app.run(debug=True)


# - app.run() launches the built-in Flask server so your app can start receiving
#requests. By default, it runs on http://127.0.0.1:5000/.
# - Setting debug = True gives you auto-reload such that you don't have to restart the server
#after making changes to your code. And it also provides you with an interactive debugger. That is,
#Flask shows you an interactive error page in the browser if your app crashes or throws an error.
# - Never use debug = True in production, because it exposes internal info to users and it can be 
#a security risk. Only use it during development, as it helps you build faster and debug easier.
