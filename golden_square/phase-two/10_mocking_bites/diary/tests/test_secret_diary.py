from lib.secret_diary import SecretDiary
from unittest.mock import Mock
import pytest

"""
On init, a diary is locked and attempting to read it without unlocking
Raise error "Go away!"

When we unlock the diary
Return the diary's contents
"""

def test_adding_mock_diary_to_secret_diary():
    fake_diary = Mock()
    fake_diary.read.return_value = "it's a secret ... ssshut upppp"
    secret = SecretDiary(fake_diary)
    with pytest.raises(Exception) as error:
        secret.read()
    assert str(error.value) == 'Go away!'
    fake_diary.read.asset_not_called()

    secret.unlock()
    assert secret.read() == "it's a secret ... ssshut upppp"
    fake_diary.read.assert_called()

    secret.lock()
    with pytest.raises(Exception) as error:
        secret.read()
    assert str(error.value) == 'Go away!'