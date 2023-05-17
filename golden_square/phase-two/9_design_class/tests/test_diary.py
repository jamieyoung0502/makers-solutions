from lib.diary import Diary
import pytest

"""
When no diary entries, numbers or tasks have been added
I see an empty list
"""

def test_diary_empty_entry_lists_on_init():
    diary = Diary()
    assert diary.list_item("entries") == []

"""
When I ask to see a list that does not exist
I receive an error
"""

def test_diary_list_invalid_item():
    diary = Diary()
    with pytest.raises(ValueError) as error:
        diary.list_item("homework")
    error_message = str(error.value)
    assert error_message == "Invalid item type"

"""
When I add an item for which there isn't a class
I receive an error
"""

def test_diary_add_invalid_item():
    diary = Diary()
    with pytest.raises(ValueError) as error:
        diary.add_item("homework")
    error_message = str(error.value)
    assert error_message == "Invalid item type"

"""
When there are no diary entries and I want some suggested reading
Return None
"""

def test_diary_no_suggested_entry_when_empty():
    diary = Diary()
    assert diary.suggest_entry(1, 1) == None
