from lib.book_repo import BookRepository
from lib.book import Book

"""
When we call BookRepository#all
We get a list of Book objects reflecting the seed data.
"""
def test_all_records(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    books = repository.all()

    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]

"""
When we call BookRepository#find
We get a single Book object reflecting the seed data.
"""

def test_find_specific_book(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    book = repository.find(1)
    assert book == Book(1, 'Nineteen Eighty-Four', 'George Orwell')


"""
When we call BookRepository#create
We get a new record in the database.
"""
def test_create_new_book(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    repository.create(Book(None, "How to Code for dummies", "Adrian Hards"))

    books = repository.all()
    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton'),
        Book(6, "How to Code for dummies", "Adrian Hards")
    ]

"""
When we call BookRepository#update
We update a record in the database.
"""
def test_update_a_book(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    new_book = Book(None, "How to Code for dummies", "Adrian Hards")
    repository.create(new_book)
    new_book.title = "Python for Dum Dums"
    repository.update(new_book, 6)

    books = repository.all()
    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton'),
        Book(6, "Python for Dum Dums", "Adrian Hards")
    ]

    # repository.update("author_name", "adrianHards", 6)
    # books = repository.all()
    # assert books == [
    #     Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
    #     Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
    #     Book(3, 'Emma', 'Jane Austen'),
    #     Book(4, 'Dracula', 'Bram Stoker'),
    #     Book(5, 'The Age of Innocence', 'Edith Wharton'),
    #     Book(6, "Python for Dum Dums", "adrianHards")
    # ]


"""
When we call BookRepository#delete
We remove a record from the database.
"""

def test_delete_a_book(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    repository.create(Book(None, "Python for Dum Dums", "Adrian Hards"))

    books = repository.all()
    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton'),
        Book(6, "Python for Dum Dums", "Adrian Hards")
    ]

    repository.delete(6)
    books = repository.all()
    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]