import pytest
from lib.make_snippet import make_snippet

"""
If we give an empty string
return "can't pass an empty string"
"""

def test_make_snipper_empty_string():
    with pytest.raises(Exception) as error:
        make_snippet("")
    result = str(error.value)
    assert result == "can't pass an empty string"

"""
If we pass five words "hello hello hello hello hello"
Returns "hello hello hello hello hello"
"""

def test_make_snipper_five_words():
    actual = make_snippet("hello hello hello hello hello")
    expected = "hello hello hello hello hello"
    assert actual == expected

"""
If we pass five words "hello hello hello hello hello hello hello hello hello hello"
Returns "hello hello hello hello hello ..."
"""

def test_make_snipper_more_than_five_words():
    text = ("hello " * 10).strip()
    actual = make_snippet(text)
    expected = "hello hello hello hello hello ..."
    assert actual == expected