import pytest
from lib.count_words import count_words

"""
if empty string given
returns 0
"""

def test_empty_string_returns_zero():
    result = count_words("")
    assert result == 0

"""
if two words separated by empty whitespace are given
returns 2
"""

def test_two_lowercase_words_separated_by_whitespaces__returns_two():
    result = count_words("hello world")
    assert result == 2


"""
if two words separated by commas are given
returns 2
"""

def test_two_lowercase_words_separated_by_commas_returns_two():
    result = count_words("hello,world")
    assert result == 2

"""
if two words with upper and lowercase chars, and separated by commas are given
returns 2
"""

def test_two_mixed_case_words_separated_by_commas_returns_two():
    result = count_words("hEllo,World")
    assert result == 2

"""
if string not given
returns TypeError
"""

def test_if_wrong_data_type_given_raises_type_error():
    with pytest.raises(TypeError) as error:
        count_words(None)
    error_message = str(error.value)
    assert error_message == f"Expected a string but got {type(None).__name__}"