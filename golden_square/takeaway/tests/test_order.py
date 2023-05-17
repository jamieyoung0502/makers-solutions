from lib.order import Order
from lib.dish import Dish
from unittest.mock import Mock
import pytest

"""
When there are no dishes
Returns an empty dictionary
"""
def test_empty_order_dishes():
    order = Order()
    assert order.dishes == {}, "dishes should be an empty dictionary on init"

"""
When mock dishes are added
Returns a dictionary of Mock dishes
"""
def test_add_dishes_to_order():
    dish_1, dish_2, dish_3 = Mock(spec=Dish), Mock(spec=Dish), Mock(spec=Dish)

    dish_1.title = "hamburger"
    dish_1.price = 7.75
    dish_2.title = "pizza"
    dish_2.price = 15.5
    dish_3.title = "fries"
    dish_3.price = 2.25

    order = Order()
    order.add_to_order(dish_1)
    order.add_to_order(dish_2)
    order.add_to_order(dish_3)

    assert order.dishes == {
        "hamburger" : {"price" : 7.75, "quantity" : 1, "sum" : 7.75},
        "pizza" : {"price" : 15.5, "quantity" : 1, "sum" : 15.5},
        "fries" : {"price" : 2.25, "quantity" : 1, "sum" : 2.25},
    }

"""
When an item already in the dictionary is added
The dish is not added to the dictionary but the number of that dish goes up by one
"""

def test_add_same_dish_multiple_times():
    dish_1, dish_2, dish_3 = Mock(spec=Dish), Mock(spec=Dish), Mock(spec=Dish)

    dish_1.title = "hamburger"
    dish_1.price = 7.75
    dish_2.title = "hamburger"
    dish_2.price = 7.75
    dish_3.title = "fries"
    dish_3.price = 2.25

    order = Order()
    order.add_to_order(dish_1)
    order.add_to_order(dish_2)
    order.add_to_order(dish_3)

    assert order.dishes == {
        "hamburger" : {"price" : 7.75, "quantity" : 2, "sum" : 15.5},
        "fries" : {"price" : 2.25, "quantity" : 1, "sum" : 2.25},
    }

"""
When anything other than an instance of Dish is added
An error is thrown
"""

def test_not_instance_of_dish():
    dish = Mock()
    order = Order()
    with pytest.raises(ValueError) as error:
        order.add_to_order(dish)
    assert str(error.value) == 'Only Dish instances can be added'


