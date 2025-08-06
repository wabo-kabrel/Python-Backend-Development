from flask import Flask, request, jsonify
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Connecting to the database
def get_db_connection():
    # Creates a connection to the SQLite database 'books.db'
    # Sets the row_factory to sqlite3.Row to access columns by name
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

# Creating the books table if it doesn't exist
def create_books_table():
    # Establish a database connection
    conn = get_db_connection()
    # Execute a SQL query to create the 'books' table with the following columns:
    # id (primary key), author (text), language (text), title (text)
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
    conn.commit()  # Save (commit) the changes
    conn.close()   # Close the connection to free up resources

# Call the function to ensure the table is created on app start
create_books_table()

# Route to handle GET and POST requests for books
@app.route('/books', methods=['GET', 'POST'])
def books():
    # Open a new database connection for this request
    conn = get_db_connection()

    if request.method == 'GET':
        # Fetching all the books from the database
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')  # SQL to retrieve all book records
        books = cursor.fetchall()  # Get all rows from the query
        conn.close()  # Close the connection

        if books:
            # Converting the book data into a list of dictionaries
            books_list = []
            for book in books:
                # Each book is represented as a dictionary with id, author, language, and title
                books_list.append({
                    'id': book['id'],
                    'author': book['author'],
                    'language': book['language'],
                    'title': book['title']
                })
            return jsonify(books_list)  # Return the list as a JSON response
        else:
            # If no books found, return a 404 message
            return jsonify({'message': 'No books found'}), 404

    elif request.method == 'POST':
        # Getting form data from the request
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']

        # Inserting the new book into the database
        sql = 'INSERT INTO books (author, language, title) VALUES (?, ?, ?)'
        conn.execute(sql, (new_author, new_lang, new_title))  # Use placeholders to prevent SQL injection
        conn.commit()  # Save the new book into the database
        conn.close()   # Close the connection

        # Return success message with 201 status code
        return jsonify({'message': 'Book added successfully!'}), 201


@app.route('/book/<int:id>', methods=["GET", "PUT", "DELETE"])
def single_book(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    book = None

    if request.method == "GET":
        cursor.execute("SELECT * FROM books WHERE id=?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            book = {
                'id': row['id'],
                'author': row['author'],
                'language': row['language'],
                'title': row['title']
            }
            return jsonify(book), 200
        else:
            return jsonify({'message': 'Book not found'}), 404

    if request.method == "PUT":
        sql = "UPDATE books SET author=?, language=?, title=? WHERE id=?"
        author = request.form['author']
        language = request.form['language']
        title = request.form['title']
        updated_book = {
            'id': id,
            'author': author,
            'language': language,
            'title': title
        }
        conn.execute(sql, (author, language, title, id))
        conn.commit()
        conn.close()
        return jsonify(updated_book), 200

    if request.method == "DELETE":
        sql = "DELETE FROM books WHERE id=?"
        conn.execute(sql, (id,))
        conn.commit()
        conn.close()
        return f"The book with id: {id} has been deleted.", 200

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for easier development and troubleshooting


# For better understanding, visit https://youtu.be/HX-ChCQfJEo?si=Ih2R4xgwFUkTl8pK