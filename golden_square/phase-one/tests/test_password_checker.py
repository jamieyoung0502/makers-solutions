import pytest
from lib.password_checker import PasswordChecker


def test_password_checker_returns_true_for_valid_password():
    checker = PasswordChecker()
    result = checker.check("password")
    assert result == True


def test_password_checker_returns_error_for_invalid_password():
    checker = PasswordChecker()
    with pytest.raises(Exception) as error:
        checker.check("pass")
    error_message = str(error.value)
    assert error_message == "Invalid password, must be 8+ characters."


def test_password_checker_only_accepts_a_string():
    checker = PasswordChecker()
    list_type = [1, 2, 3, 4, 5, 6, 7, 8]
    with pytest.raises(TypeError) as error:
        checker.check(list_type)
    error_message = str(error.value)
    assert error_message == f"Expected a string but got {type(list_type).__name__}"
