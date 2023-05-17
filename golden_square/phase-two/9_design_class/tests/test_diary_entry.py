from lib.diary_entry import DiaryEntry

"""
When I create a diary entry with no phone number
Diary entry numbers returns an empty list
"""

def test_diary_entry_init_with_empty_numbers():
    entry = DiaryEntry("title", "contents")
    assert entry.numbers == []

"""
When I create a diary entry with a phone number
The phone number is correctly extracted from the contents and saved to self.numbers
"""

def test_diary_entry_extracts_valid_number():
    entry = DiaryEntry("title", "contents with 07800000001")
    assert entry.numbers == ["07800000001"]


"""
When I create a diary entry with non-valid phone numbers
These numbers are not extracted from the diary entry
"""

def test_diary_entry_invalid_numbers_ignored():
    entry = DiaryEntry("title", "contents 123")
    assert entry.numbers == []


"""
When I create a diary entry with a phone number
It ignores invalid numbers and extracts valid number only
"""

def test_diary_entry_extracts_valid_ignores_invalid_numbers():
    entry = DiaryEntry("title", "contents with 123 07800000001")
    assert entry.numbers == ["07800000001"]

"""
When I create a diary entry with two valid phone numbers
Both numbers are added
"""

def test_diary_entry_extracts_two_valid_numbers():
    entry_1 = DiaryEntry("title", "contents with 123 07800000001 07800000002")
    assert entry_1.numbers == ["07800000001", "07800000002"]

