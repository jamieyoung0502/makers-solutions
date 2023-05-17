# Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can improve my grammar
> I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def grammar_checker(text: str) -> bool:
    # Parameters:
    #   text: a sentence string containing words and punctuation
    #   e.g. "Hello, world!"
    # Returns:
    #   bool: sentence starts with a capital letter and ends with either !.?
    #   e.g. the above returns True
    #   alterntively could return a string:
    #   "first letter is not capitalised"
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Empty string
returns False
"""

def test_empty_string():
    result = grammar_checker("")
    assert result == False

"""
Starts with a capital letter and has a full stop
returns True
"""

def test_starts_with_capital_letter_has_full_stop():
    result = grammar_checker("Hello world.")
    assert result == True

"""
No capital letter but has a full stop
returns False
"""

def test_does_not_start_with_capital_letter_has_full_stop():
    result = grammar_checker("hello world.")
    assert result == False

"""
Starts with capital letter but has no full stop
returns False
"""

def test_starts_with_capital_letter_no_full_stop():
    result = grammar_checker("Hello world")
    assert result == False

"""
Has full stop and a capital letter but not at the start
returns False
"""

def test_wrong_capital_letter_location_has_full_stop():
    result = grammar_checker("heLLo world.")
    assert result == False

"""
Starts with capital letter but ends in incorrect punctuation
returns False
"""

def test_capital_letter_but_incorrect_punctuation():
    result = grammar_checker("Hello world,")
    assert result == False

"""
Wrong data type given
returns False
"""

def test_incorrect_data_type():
    with pytest.raises(TypeError) as error:
        grammar_checker(['Hello world.'])
    error_message = str(error.value)
    assert error_message == f"Expected a string but got {type(list_type).__name__}"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python
# EXAMPLE
```

Ensure all test function names are unique, otherwise pytest will ignore them!
