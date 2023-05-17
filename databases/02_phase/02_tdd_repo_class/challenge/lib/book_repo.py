from lib.book import Book

class BookRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from books')
        return [Book(row["id"], row["title"], row["author_name"]) for row in rows]

    def find(self, book_id):
        query = """
        SELECT *
        FROM books
        WHERE id = %s
        """
        book = self._connection.execute(query, [book_id])[0]
        return Book(book["id"], book["title"], book["author_name"])

    def create(self, book):
        query = """
        INSERT INTO books
        (title, author_name)
        VALUES (%s, %s)
        """
        book = self._connection.execute(query, [book.title, book.author_name])

    # def update(self, col_name, new_value, book_id):
    #     query = """
    #     UPDATE books
    #     SET {} = %s
    #     WHERE id = %s;
    #     """.format(col_name)


    #     # better to update the whole thing rather than one specific column!

    #     self._connection.execute(query, [new_value, book_id])

    def update(self, book, book_id):
        query = """
        UPDATE
            books
        SET
            title = %s,
            author_name = %s
        WHERE
            id = %s;
        """

        values = (
        book.title,
        book.author_name,
        book_id
        )

        self._connection.execute(query, values)

    def delete(self, book_id):
        query = """
        DELETE FROM books
        WHERE id = %s;
        """
        self._connection.execute(query, [book_id])