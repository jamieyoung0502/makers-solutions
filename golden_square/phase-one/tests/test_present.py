import pytest
from lib.present import Present

# with is used to wrap the execution of a block of code with methods defined by a context manager
# A context manager is an object that defines the methods __enter__() and __exit__(), which are called when a block of code is entered and exited, respectively.
# The with statement ensures that the context manager is properly initialized before the code inside the block is executed, and that the __exit__() method is called even if an exception is raised during the execution of the block.
# This is useful for releasing resources such as file handles, network connections, and locks that were acquired in the __enter__() method, even if the code inside the with block raises an exception.


def test_present_already_wrapped_contents():
    contents = Present()
    contents.wrap("gift")

    # with pytest.raises() block captures the exception and allows you to make assertions about the exception.
    with pytest.raises(Exception) as error:
        contents.wrap("coal")
    # The captured exception is stored in the error variable, which you can use to make assertions about the exception
    error_message = str(error.value)
    assert error_message == "A contents has already been wrapped."


def test_present_no_contents():
    contents = Present()

    with pytest.raises(Exception) as error:
        contents.unwrap()
    error_message = str(error.value)
    assert error_message == "No contents have been wrapped."


def test_present_wrap_twice_preserves_old_contents():
    contents = Present()
    contents.wrap("gift")
    with pytest.raises(Exception) as error:
        contents.wrap("coal")
    assert contents.unwrap() == "gift"
