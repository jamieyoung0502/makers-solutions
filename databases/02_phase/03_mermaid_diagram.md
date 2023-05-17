```python
# Table name: books

# Model class
# (in lib/book.py)
class Book
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

# Repository class
# (in lib/book_repository.py)
class BookRepository
    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT * FROM books;
        # Returns an array of Book objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(book_id):
        # Executes the SQL query:
        # SELECT * FROM books WHERE id = %s;
        # Returns a single Book object.

    # Creates single record of Book
    # One argument: Book object
    def create(book):
        # Executes the SQL query:
        # INSERT INTO books (title, author) VALUES (%s, %s)
        # Returns a single Book object.

    # Updates a single record of Book
    # One argument: id
    def update(col_name, new_value, book_id)
        # Executes the SQL query:
        # UPDATE books SET %s = %s  WHERE id = %s;
        # Returns a single Book object.

    # Destroys a single record of Book
    # One argument: id
    def delete(book_id)
        # Executes the SQL query:
        # DELETE FROM books WHERE id = %s;
        # Returns a single Book object.

```

```mermaid
sequenceDiagram
    participant t as Terminal
    participant app as Main program (app.py)
    participant ar as BookRepository class <br /> (in lib/book_repository.py)
    participant db_conn as DatabaseConnection class <br /> (in lib/database_connection.py)
    participant db as Postgres database

    %% Note left of t: Flow of time <br />⬇ <br /> ⬇ <br /> ⬇

    t->>app: Run `python app.py`
    app->>db_conn: Opens connection to database calling method `connect` on DatabaseConnection
    db_conn->>db_conn: Opens database connection using PG and stores the connection
    app->>db: Populates the database with the given SQL file calling method 'seed' on DatabaseConnection
    app->>ar: Calls method `all` on BookRepository
    ar->>db_conn: Sends SQL query by calling method `execute` on DatabaseConnection
    db_conn->>db: Sends query to database via the open database connection
    db->>db_conn: Returns a list of dictionaries, one for each row of the books table

    db_conn->>ar: Returns a list of dictionaries, one for each row of the books table
    loop
        ar->>ar: Loops through list and creates a Book object for every row
    end
    ar->>app: Returns list of Book objects
    app->>t: Prints list of books to terminal
```
