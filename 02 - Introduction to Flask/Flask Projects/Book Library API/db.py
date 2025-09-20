from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connecting to the database
def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

# Creating the books table if it doesn't exist
def create_books_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT NOT NULL,
            language TEXT NOT NULL,
            title TEXT NOT NULL
        )
    ''')
                                # Executing the query. Running python db.py
                                # will now create the database.
                                # After creating the database, you can view it using
                                # DataGrip or using the VS Code extension, SQLite Viewer by
                                # Florian Klampfer.
    conn.commit()
    conn.close()

create_books_table()

# Route to handle GET and POST requests for books
@app.route('/books', methods=['GET', 'POST'])
def books():
    conn = get_db_connection()

    if request.method == 'GET':
        # Fetching all the books from the database
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
        conn.close()

        if books:
            # Converting the book data into a list of dictionaries
            books_list = []
            for book in books:
                books_list.append({
                    'id': book['id'],
                    'author': book['author'],
                    'language': book['language'],
                    'title': book['title']
                })
            return jsonify(books_list)
        else:
            return jsonify({'message': 'No books found'}), 404

    elif request.method == 'POST':
        # Getting form data from the request
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']

        # Inserting the new book into the database
        sql = 'INSERT INTO books (author, language, title) VALUES (?, ?, ?)'
        conn.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Book added successfully!'}), 201

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)
