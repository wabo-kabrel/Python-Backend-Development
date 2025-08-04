from flask import Flask, request, jsonify
# - Flask will provide the application instance
# - request will alow us to add methods to routes
# - jsonify will encode python dictionary into dictionary strings


app = Flask(__name__)

books_list=[
     {
         'id':0,
         "author":"Chinua Achebe",
         "language":"English",
         "title":"Things Fall Apart",
     },
     {
         'id': 1,
         "author": "Hans Christian Andersen",
         "language": "Danish",
         "title": "Fairy Tales",
     },
     {
         'id': 2,
         "author": "Samuel Beckett",
         "language": "French,English",
         "title": "Molloy,Malone Dies,The Unnamable,The Triology",
     },
     {
         'id': 6,
         "author": "Jorge Luis Borges",
         "language": "Spanish",
         "title": "Ficciones",
     },
     {
         'id': 3,
         "author": "Giovanni Boccaccio",
         "language": "Italian",
         "title": "The Decameron",
     },
     {
         'id': 5,
         "author": "Emily Bront",
         "language": "English",
         "title": "Wuthering Heights",
     },
 ]