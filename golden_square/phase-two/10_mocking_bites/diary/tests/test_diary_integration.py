from lib.secret_diary import SecretDiary
from lib.diary import Diary
import pytest

"""
A diary added to the secret diary is locked;
Attempting to read it without unlocking it first is not possible;
Raise error "Go away!"

When we unlock the diary;
Return the diary's contents
"""

def test_adding_diary_to_secret_diary():
    diary = Diary("it's a secret ... ssshut upppp")
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as error:
        secret_diary.read()
    assert str(error.value) == 'Go away!'

    secret_diary.unlock()
    assert secret_diary.read() == "it's a secret ... ssshut upppp"

    secret_diary.lock()
    with pytest.raises(Exception) as error:
        secret_diary.read()
    assert str(error.value) == 'Go away!'