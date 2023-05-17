from lib.customer import Customer

"""
does the class construct an object
and can attributes be called
"""


def test_constructs_object():
    customer = Customer(1, "Adrian", "Hards")
    assert customer.id == 1
    assert customer.first_name == "Adrian"
    assert customer.last_name == "Hards"


"""
when printed are the objects formatted in a readable manner
"""


def test_printed_object_is_formatted():
    customer = Customer(1, "Adrian", "Hards")
    assert str(customer) == "Customer(id=1, first_name='Adrian', last_name='Hards')"


"""
are two objects with the same attributes regarded as equal
"""


def test_objects_with_same_attributes_seen_as_equal():
    customer_1 = Customer(1, "Adrian", "Hards")
    customer_2 = Customer(1, "Adrian", "Hards")
    assert customer_1 == customer_2
