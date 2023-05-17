from lib.menu import Menu
from unittest.mock import Mock

"""
When there are no dishes
Returns an empty list
"""

def test_empty_dishes():
    menu = Menu()
    assert menu.list_dishes() == []

"""
When mock dishes are added
Returns a list of dishes showing their name and price
"""


def test_add_multiple_dishes():
    dish_1, dish_2, dish_3 = Mock(), Mock(), Mock()

    dish_1.title = "hamburger"
    dish_1.price = 7.75
    dish_2.title = "pizza"
    dish_2.price = 15.5
    dish_3.title = "fries"
    dish_3.price = 2.25

    menu = Menu(dish_1, dish_2, dish_3)

    assert menu.dishes == [dish_1, dish_2, dish_3]
    assert menu.list_dishes() == ["Hamburger for £7.75", "Pizza for £15.5", "Fries for £2.25"]
