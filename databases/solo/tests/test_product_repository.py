from lib.product_repository import ProductRepository
from lib.product import Product

"""
when I call ProductRepository#all
I see a list of all products for sale, their price and stock
no stock should be less than 0
"""


def test_product_repository_all(db_connection):
    db_connection.seed("seeds/supermarket.sql")
    repository = ProductRepository(db_connection)
    all_result = repository.all()

    assert all_result == [
        Product(1, "salad cream", 100, 9.99),
        Product(2, "ketchup", 0, 8.01),
        Product(3, "mayo", 11, 5),
    ]


"""
when I call ProductRepository#create
I can add a new product to my inventory if the values are valid
and see the product added to my inventory
"""


def test_create_new_product(db_connection):
    db_connection.seed("seeds/supermarket.sql")
    repository = ProductRepository(db_connection)
    new_product = Product(None, "HP sauce", 100, 6.45)
    create_result = repository.create(new_product)

    assert create_result == None

    all_result = repository.all()

    assert all_result == [
        Product(1, "salad cream", 100, 9.99),
        Product(2, "ketchup", 0, 8.01),
        Product(3, "mayo", 11, 5),
        Product(4, "HP sauce", 100, 6.45),
    ]
