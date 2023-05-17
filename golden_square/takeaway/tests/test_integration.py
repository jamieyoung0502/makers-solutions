from lib.menu import Menu
from lib.dish import Dish
from lib.order import Order
from lib.receipt import Receipt
from lib.sms import SMS

import pytest
from twilio.rest import Client

@pytest.fixture
def setup_menu():
    hamburger = Dish("hamburger", 7.75)
    pizza = Dish("pizza", 15.5)
    fries = Dish("fries", 2.25)

    menu = Menu(hamburger, pizza, fries)

    yield menu, hamburger, pizza, fries

@pytest.fixture
def setup_order(setup_menu):
    menu, hamburger, pizza, fries = setup_menu
    order = Order()
    order.add_to_order(hamburger)
    order.add_to_order(hamburger)
    order.add_to_order(fries)
    order.add_to_order(fries)
    order.add_to_order(pizza)

    yield order

"""
When I ask to see the menu
I see a list of dishes (their name and price)
"""
def test_menu_see_dishes(setup_menu):
    menu, hamburger, pizza, fries = setup_menu
    assert menu.list_dishes() == ["Hamburger for £7.75", "Pizza for £15.5", "Fries for £2.25"]
    assert menu.dishes == [hamburger, pizza, fries]

"""
I can add dishes to my order, some in duplicate
"""

def test_order_add_dishes(setup_menu):
    menu, hamburger, pizza, fries = setup_menu
    order = Order()
    order.add_to_order(hamburger)
    order.add_to_order(hamburger)
    order.add_to_order(fries)
    order.add_to_order(fries)
    order.add_to_order(pizza)

    assert order.dishes == {
        "hamburger" : {"price" : 7.75, "quantity" : 2, "sum" : 15.5},
        "pizza" : {"price" : 15.5, "quantity" : 1, "sum" : 15.5},
        "fries" : {"price" : 2.25, "quantity" : 2, "sum" : 4.5},
    }

"""
Once I have confirmed my order I ask for an itemised receipt
Returns the total amount I owe for all of the dishes I have ordered
"""
def test_itemised_receipt_for_order(setup_order):
    order = setup_order
    receipt = Receipt(order)

    assert receipt.order == order
    assert receipt.grand_total() == "35.50"

"""
Once I have submitted my order
I receive SMS confirmation as an itemised receipt
"""
def test_send_sms(setup_order):
    order = setup_order
    receipt = Receipt(order)
    sms = SMS(receipt, Client)

    expected_body = "\nThank you for your order! You ordered:\n2 hamburgers for £15.5\n2 fries for £4.5\n1 pizza for £15.5\n***\nFor a total of: 35.50\n***"
    assert sms._body_message() == expected_body
    # sms.send()


