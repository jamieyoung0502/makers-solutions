from lib.book import Book

"""
creates an instance of Book with id, title and author
"""
def test_create_book():
    book = Book(1, "How to Code for dummies", "Adrian Hards")
    assert book.id == 1
    assert book.title == "How to Code for dummies"
    assert book.author_name == "Adrian Hards"


"""
We can format books to strings nicely
"""
def test_books_format_nicely():
    book = Book(1, "How to Code for dummies", "Adrian Hards")
    assert str(book) == "Book(id=1, title='How to Code for dummies', author_name='Adrian Hards')"


"""
We can compare two identical books
And have them be equal
"""

def test_two_books_are_equal():
    book_1 = Book(1, "How to Code for dummies", "Adrian Hards")
    book_2 = Book(1, "How to Code for dummies", "Adrian Hards")
    assert book_1 == book_2