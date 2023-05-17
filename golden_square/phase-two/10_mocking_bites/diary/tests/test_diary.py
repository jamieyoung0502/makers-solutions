from lib.diary import Diary

"""
After creating a diary with contents, we read the diary
Returns the diary's contents
"""

def test_read_diary():
    diary = Diary("it's a secret ... ssshut upppp")
    assert diary.read() == "it's a secret ... ssshut upppp"