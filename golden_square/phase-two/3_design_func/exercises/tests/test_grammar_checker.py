import pytest
from lib.grammar_checker import grammar_checker

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
    assert error_message == f"Expected a string but got {type(['Hello world.']).__name__}"

