from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'     # use a SQLite database stored in a 
                                                                    #file named database.db.
db = SQLAlchemy(app)        # SQLAlchemy(app) connects the app to the database.
api = Api(app)

class UserModel(db.Model):          # Defines a model ( a table in the database called UserModel)
    id = db.Column(db.Integer, primary_key=True)        # id is the primary key
    name = db.Column(db.String(80), unique=True, nullable=False)    # name is a column in the table
    email = db.Column(db.String(80), unique=True, nullable=False)   # email is a column in the table
    def __repr__(self):         # returns a string representation of the object in the database.
        return f"User(name = {self.name}, email = {self.email})"
    
user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, help='Name cannot be blank', required=True)
user_args.add_argument('email', type=str, help='Email', required=True)

userFields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'email' : fields.String
}

class Users(Resource):
     @marshal_with(userFields)
     def get(self):
         users = UserModel.query.all() 
         return users
     
     @marshal_with(userFields)
     def post(self):
         args = user_args.parse_args()
         user = UserModel(name=args["name"], email=args["email"])
         db.session.add(user)
         db.session.commit()
         users = UserModel.query.all()
         return users, 201


api.add_resource(Users, '/api/users')

# The route is used to request data from the server.
# The data is requested using a URL.
# The response is sent back to the client (browser).
@app.route('/')     # A slash / comes after the domain 
def home():
    return '<h1>Flask Rest API</h1>'

if __name__ == '__main__':
    app.run(debug=True)
    

# - app.run() launches the built-in Flask server so your app can start receiving
#requests. By default, it runs on http://127.0.0.1:5000/.
# - Setting debug = True gives you auto-reload such that you don't have to restart the server
#after making changes to your code. And it also provides you with an interactive debugger. That is,
#Flask shows you an interactive error page in the browser if your app crashes or throws an error.
# - Never use debug = True in production, because it exposes internal info to users and it can be 
#a security risk. Only use it during development, as it helps you build faster and debug easier.