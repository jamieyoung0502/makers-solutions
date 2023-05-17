# Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can keep track of my tasks
> I want to check if a text includes the string '#TODO'.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def todo_checker(text: str) -> bool:
    # Parameters:
    #   text: a task (string) that contains the word TODO
    #   e.g. "I need to do groceries #TODO"
    # Returns:
    #   bool: if the string contains the key word #TODO
    #   True
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Empty string
Return False
"""

def test_empty_string():
    todo_checker("")
    # => False

"""
If data type is not a string
Raise a TypeError
"""

def test_wrong_data_type():
    todo_checker(['#TODO'])
    # => TypeError

"""
Enter a string without #TODO
Return False
"""

def test_string_without_todo():
    todo_checker("do the dishes")
    # => False

"""
Enter a string with #TODO
Return True
"""

def test_string_with_todo():
    todo_checker("do the dishes #TODO")
    # => True

"""
Enter a string with the chars of #TODO out of order
Return False
"""

def test_string_with_invalid_order_of_chars_todo():
    todo_checker("#I need TO DO the dishes")
    # => False

"""
Enter a string with #TODO but not isolated from the rest of the text
Return False
"""

def test_string_with_todo_connected_to_rest_of_text():
    todo_checker("do the dishes#TODO")
    # => True

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python
# EXAMPLE
```

Ensure all test function names are unique, otherwise pytest will ignore them!
