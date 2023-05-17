import pytest
from lib.make_snipper import make_snipper

"""
if given an empty string
returns empty string
"""

def test_string_with_less_than_5_words_returns_all_words():
    test_string = ""
    result = make_snipper(test_string)
    assert result == test_string


"""
if less than 5 words in the string
returns the string
"""

def test_string_with_less_than_5_words_returns_all_words():
    test_string = "less than five words"
    result = make_snipper(test_string)
    assert result == test_string

"""
if more than 5 words in the string
returns the first 5 words then ...
"""

def test_string_with_more_than_5_words_returns_first_5_words_then_ellipsis():
    test_string = "this is a lot more than five words"
    result = make_snipper(test_string)
    assert result == "this is a lot more..."

"""
if something other than a string is given
raises a TypeError
"""

def test_if_wrong_data_type_used_raises_type_error():
    with pytest.raises(TypeError) as error:
        make_snipper(None)
    error_message = str(error.value)
    assert error_message == f"Expected a string but got {type(None).__name__}"