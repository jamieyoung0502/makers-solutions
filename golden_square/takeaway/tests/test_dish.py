import pytest
from lib.dish import Dish

"""
When creating a dish with str for price
An error is thrown
"""
def test_string_for_price():
    with pytest.raises(Exception) as error:
        Dish("hamburger", "7.75")
    assert str(error.value) == 'enter a float for price'


"""
When a dish is created with an integer for price
The price is converted into a float
"""
def test_int_for_price():
    dish = Dish("hamburger", 7)
    assert isinstance(dish.price, float)


"""
When a dish is created with None for title
An error is thrown
"""
def test_none_for_title():
    with pytest.raises(Exception) as error:
        Dish(None, 7.75)
    assert str(error.value) == 'enter a string for title'

"""
When a dish is created with an empty string
An error is thrown
"""
def test_empty_string_for_title_or_price():
    with pytest.raises(Exception) as error:
        Dish("", 7.75)
    assert str(error.value) == 'enter a valid title and price'

    with pytest.raises(Exception) as error:
        Dish("hamburger", "")
    assert str(error.value) == 'enter a valid title and price'

"""
When a dish is created with a price equal to or less than zero
An error is thrown
"""
def test_zero_or_less_for_price():
    with pytest.raises(Exception) as error:
        Dish("hamburger", 0)
    assert str(error.value) == 'enter a float greater than 0 for price'

    with pytest.raises(Exception) as error:
        Dish("hamburger", -1)
    assert str(error.value) == 'enter a float greater than 0 for price'

    with pytest.raises(Exception) as error:
        Dish("hamburger", -1.5)
    assert str(error.value) == 'enter a float greater than 0 for price'