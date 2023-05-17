from lib.product import Product

"""
does the class construct an object
and can attributes be called
"""


def test_constructs_object():
    product = Product(1, "ketchup", 10, 5.5)
    assert product.id == 1
    assert product.name == "ketchup"
    assert product.quantity == 10
    assert product.price == 5.5


"""
when printed are the objects formatted in a readable manner
"""


def test_printed_object_is_formatted():
    product = Product(1, "ketchup", 10, 5.5)
    assert str(product) == "Product(id=1, name='ketchup', quantity=10, price=5.5)"


"""
are two objects with the same attributes regarded as equal
"""


def test_objects_with_same_attributes_seen_as_equal():
    product_1 = Product(1, "ketchup", 5.5, 10)
    product_2 = Product(1, "ketchup", 5.5, 10)
    assert product_1 == product_2
