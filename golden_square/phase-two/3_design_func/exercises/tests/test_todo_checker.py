import pytest
from lib.todo_checker import todo_checker

"""
Empty string
Return False
"""

def test_empty_string():
    result = todo_checker("")
    assert result == False

"""
If data type is not a string
Raise a TypeError
"""

def test_wrong_data_type():
    with pytest.raises(TypeError) as error:
        todo_checker(['#TODO'])
    error_message = str(error.value)
    assert error_message == f"Expected a string but got {type(['#TODO']).__name__}"

"""
Enter a string without #TODO
Return False
"""

def test_string_without_todo():
    result = todo_checker("do the dishes")
    assert result == False

"""
Enter a string with #TODO
Return True
"""

def test_string_with_todo():
    result = todo_checker("do the dishes #TODO")
    assert result == True

"""
Enter a string with the chars of #TODO out of order
Return False
"""

def test_string_with_invalid_order_of_chars_todo():
    result = todo_checker("#I need TO DO the dishes")
    assert result == False

"""
Enter a string with #TODO but not isolated from the rest of the text
Return False
"""

def test_string_with_todo_connected_to_rest_of_text():
    result = todo_checker("do the dishes#TODO")
    assert result == True
