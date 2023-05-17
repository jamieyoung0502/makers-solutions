from lib.order import Order

"""
does the class construct an object
and can attributes be called
"""


def test_constructs_object():
    order = Order(1, 1, "01/01/2023")
    assert order.id == 1
    assert order.customer_id == 1
    assert order.date == "01/01/2023"


"""
when printed are the objects formatted in a readable manner
"""


def test_printed_object_is_formatted():
    order = Order(1, 1, "01/01/2023")
    assert str(order) == "Order(id=1, customer_id=1, date='01/01/2023')"


"""
are two objects with the same attributes regarded as equal
"""


def test_objects_with_same_attributes_seen_as_equal():
    order_1 = Order(1, 1, "01/01/2023")
    order_2 = Order(1, 1, "01/01/2023")
    assert order_1 == order_2
