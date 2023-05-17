from lib.add_five import add_five


def test_add_give_returns_eight_for_three():
    result = add_five(3)
    assert result == 8
