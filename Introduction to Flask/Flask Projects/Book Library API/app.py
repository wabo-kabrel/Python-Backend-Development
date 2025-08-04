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

@app.route('/books', methods = ['GET', 'POST'])  # GET to get books and POST to create books
def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else: 
            'Nothing', 404

    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        iD = books_list[-1]['id']+1

        new_obj = {
            'id' : iD,
            'author' : new_author,
            'language' : new_lang,
            'title' : new_title
        }

        books_list.append(new_obj)
        return jsonify(books_list), 201
    
# Running the app
if __name__ == 'main':
    app.run()       # You can now run the app with `python app.py`