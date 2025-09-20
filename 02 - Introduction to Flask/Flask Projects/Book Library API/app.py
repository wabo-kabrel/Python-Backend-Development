# Importing necessary Flask components
from flask import Flask, request, jsonify
# - Flask will provide the application instance
# - request will alow us to add methods to routes
# - jsonify will encode python dictionary into dictionary strings


# Creating a Flask application instance
app = Flask(__name__)

# Sample in-memory list of book dictionaries, acting as the database
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

# Defining a route '/books' that accepts both GET and POST requests
@app.route('/books', methods = ['GET', 'POST'])  # GET to get books and POST to create books
def books():
     # If the client sends a GET request
    if request.method == 'GET':
        # If the books list is not empty, return the entire list as JSON
        if len(books_list) > 0:
            return jsonify(books_list)
        else: 
            # If list is empty, return an error message and status code 404 (not found)
            'Nothing', 404
    # If the client sends a POST request
    if request.method == 'POST':
         # Get data sent in form format
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        
        # Generate a new ID by incrementing the last book's ID
        iD = books_list[-1]['id']+1

        new_obj = {
            'id' : iD,
            'author' : new_author,
            'language' : new_lang,
            'title' : new_title
        }
        
        # Add the new book to the list
        books_list.append(new_obj)

        # Return the updated list and HTTP status code 201 (Created)
        return jsonify(books_list), 201
    
# Entry point: Running the app programmatically (python app.py)
if __name__ == '__main__':
    app.run()       # You can now run the app with `python app.py`

# - After running the app, the next step is to test it using Postman


"""
POSTMAN TESTING GUIDE:

1. GET All Books
   - Method: GET
   - URL: http://localhost:5000/books
   - Description: Fetch all books in the library

2. GET Single Book
   - Method: GET
   - URL: http://localhost:5000/books/<book_id>
   - Description: Replace <book_id> with the actual ID returned from a POST request

3. ADD New Book
   - Method: POST
   - URL: http://localhost:5000/books
   - Body: raw JSON
     {
       "title": "The Alchemist",
       "author": "Paulo Coelho",
       "year": 1988
     }

4. UPDATE Book
   - Method: PUT
   - URL: http://localhost:5000/books/<book_id>
   - Body: raw JSON
     {
       "title": "The Alchemist (Updated)",
       "author": "Paulo Coelho",
       "year": 1993
     }

5. DELETE Book
   - Method: DELETE
   - URL: http://localhost:5000/books/<book_id>

Tips:
- Always select 'raw' and set the body to JSON in Postman.
- Make sure the Flask server is running (python app.py).
"""

# Route for performing an operation on a single chosen book (identified from its id)
@app.route('/book/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
            pass
    elif request.method == 'PUT':
        for book in books_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['language'] = request.form['language']
                book['title'] = request.form['title']
                updated_book = {
                    'id' : id,
                    'author' : book['author'],
                    'language' : book['language'],
                    'title' : book['title']
                }
                return jsonify(updated_book)
    elif request.method == 'DELETE':
        for index, book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify(books_list)
            


# For better understanding, visit the link: https://youtu.be/8L_otSDvmR0?si=3_G0Itft7ywDw8ge