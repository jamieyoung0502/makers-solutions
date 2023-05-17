from lib.receipt import Receipt
from lib.order import Order
from unittest.mock import Mock
import pytest

"""
When anything other than an instance of Order is being added
An error is thrown
"""

def test_not_instance_of_order():
    order_mock = Mock()
    with pytest.raises(ValueError) as error:
        Receipt(order_mock)
    assert str(error.value) == 'Only an instance of the Order class can be added'

"""
When there are no dishes in an order
An error is thrown
"""

def test_empty_order():
    order_mock = Mock(spec=Order)
    order_mock.dishes = {}
    with pytest.raises(Exception) as error:
        Receipt(order_mock)
    assert str(error.value) == 'empty orders are not valid'

"""
When there is an order of each dish
The correct grand total is shown as a string to two decimal places
"""

def test_multiple_single_order_dishes():
    order_mock = Mock(spec=Order)
    order_mock.dishes = {
        "hamburger" : {"price" : 7.75, "quantity" : 1},
        "pizza" : {"price" : 15.5, "quantity" : 1},
        "fries" : {"price" : 2.25, "quantity" : 1},
    }

    receipt = Receipt(order_mock)
    assert receipt.grand_total() == "{:.2f}".format(25.5)

"""
When there are multiple orders and duplicate dishes
The correct grand total is calculated
"""

def test_multiple_duplicated_dishes():
    order_mock = Mock(spec=Order)
    order_mock.dishes = {
        "fries" : {"price" : 2.25, "quantity" : 2},
        "pizza" : {"price" : 15.5, "quantity" : 3},
        "hamburger" : {"price" : 7.75, "quantity" : 1}
    }

    receipt = Receipt(order_mock)
    assert receipt.grand_total() == "{:.2f}".format(58.75)
