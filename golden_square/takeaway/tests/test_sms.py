from lib.sms import SMS
from lib.receipt import Receipt
from unittest.mock import Mock, patch
import pytest
import os

"""
When anything other than an instance of Receipt is being added
An error is thrown
"""
def test_not_instance_of_receipt():
    twilio_mock = Mock()
    receipt_mock = Mock()
    with pytest.raises(ValueError) as error:
        SMS(receipt_mock, twilio_mock)
    assert str(error.value) == 'Only an instance of the Receipt class can be added'

"""
When there are no orders associated with an instance of Receipt
An error is thrown
"""
def test_add_receipt_with_empty_order():
    twilio_mock = Mock()
    receipt_mock = Mock(spec=Receipt)
    receipt_order_mock = receipt_mock.order = Mock()
    receipt_order_mock.dishes = {}

    with pytest.raises(Exception) as error:
        SMS(receipt_mock, twilio_mock)
    assert str(error.value) == 'empty receipts are not valid'

"""
When an order is made
Returns correct message and grand total to user's phone
"""

# In the test environment, we don't want to use the real environment variables, so we need to patch os.environ with a dictionary that contains the test values.
# This allows the test function to access the variables as if they were set in the real environment.

# When the Python interpreter encounters the @patch decorator before a function definition,
# it creates a new MagicMock object (a type of mock object) with the specified name or path.
# When the function is called, the MagicMock object is passed as an argument to the function, replacing the original object.

# os.environ is a convenient way to access the environment variables of the current process, and can be accessed and modified by any Python module running within that process
# decorators are functions which modify the functionality of other functions and are denoted by @.

@patch.dict(os.environ, {
    'TWILIO_ACCOUNT_SID': 'test_sid',
    'TWILIO_AUTH_TOKEN': 'test_token',
    'TWILIO_FROM_NUM': 'test_from_num',
    'TWILIO_TO_NUM': 'test_to_num',
})

def test_send_sms_and_body():
    receipt_mock = Mock(spec=Receipt)
    receipt_mock.grand_total.return_value = "{:.2f}".format(25.5)
    # receipt_order_mock = receipt_mock.order = Mock()
    receipt_mock.order = Mock()
    receipt_mock.order.dishes = {
        "hamburger" : {"price" : 7.75, "quantity" : 1, "sum" : 7.75},
        "pizza" : {"price" : 15.5, "quantity" : 1, "sum" : 15.5},
        "fries" : {"price" : 2.25, "quantity" : 1, "sum" : 2.25},
    }

    test_body = "\nThank you for your order! You ordered:\n1 hamburger for £7.75\n1 pizza for £15.5\n1 fries for £2.25\n***\nFor a total of: 25.50\n***"

    twilio_mock = Mock(name="twilio")
    client_mock = Mock(name="client")

    twilio_mock.return_value = client_mock

    sms = SMS(receipt_mock, twilio_mock)
    assert sms._body_message() == test_body

    sms.send()
    twilio_mock.assert_called_with('test_sid', 'test_token')
    client_mock.messages.create.assert_called_with(
        to='test_to_num',
        from_='test_from_num',
        body=test_body
    )

    message_mock = client_mock.messages.create.return_value = Mock(name="message")
    message_mock.sid.return_value = "12345"
    assert message_mock.sid() == "12345"

