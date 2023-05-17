import pytest
from lib.diary_entry import DiaryEntry

"""
lowercase title "saturday" and lowercase contents without full stop "went to the movies"
returns "Saturday: Went to the movies."
"""


def test_diary_entry_format():
    diary = DiaryEntry("saturday", "went to the movies")
    output = diary.format()
    assert output == "Saturday: Went to the movies."


"""
for a diary entry with five words "Saturday: Went to the movies."
returns integer 5
"""


def test_diary_entry_count_words():
    diary = DiaryEntry("saturday", "went to the movies")
    output = diary.count_words()
    assert output == 5


"""
for a diary entry with 1000 words and where reading time is 200 words per minute
returns integer 5
"""


def test_diary_entry_reading_time():
    wpm = 200
    contents = ("sleep " * 999).strip()
    title = "Sunday"
    diary = DiaryEntry(title, contents)
    output = diary.reading_time(wpm)
    assert output == 5


"""
for a diary entry with 1000 words and where reading time is 200 words per minute and with 2 minutes to read
returns "Sunday: " + ("sleep " * 399).strip()
"""


def test_diary_entry_reading_chunk():
    contents = ("sleep " * 999).strip()
    title = "Sunday"
    diary = DiaryEntry(title, contents)
    wpm = 200
    reading_time_mins = 2
    actual = diary.reading_chunk(wpm, reading_time_mins)
    expected = "Sunday: " + "Sleep " + ("sleep " * 398).strip()
    assert actual == expected


def test_diary_entry_reading_chunk_second_reading():
    contents = ("sleep " * 999).strip()
    title = "Sunday"
    diary = DiaryEntry(title, contents)

    wpm = 200
    first_reading_mins = 2
    diary.reading_chunk(wpm, first_reading_mins)

    second_reading_mins = 1
    actual = diary.reading_chunk(wpm, second_reading_mins)
    expected = ("sleep " * 200).strip()
    assert actual == expected


def test_diary_entry_reading_chunk_read_to_end():
    contents = ("sleep " * 999).strip()
    title = "Sunday"
    diary = DiaryEntry(title, contents)

    first_wpm = 300
    first_reading_mins = 3
    diary.reading_chunk(first_wpm, first_reading_mins)

    second_wpm = 200
    second_reading_mins = 2
    actual = diary.reading_chunk(second_wpm, second_reading_mins)
    expected = ("sleep " * 98).strip() + " sleep."
    assert actual == expected


def test_diary_entry_reading_chunk_read_to_end__then_reread():
    contents = ("sleep " * 999).strip()
    title = "Sunday"
    diary = DiaryEntry(title, contents)

    first_wpm = 1000
    first_reading_mins = 1
    diary.reading_chunk(first_wpm, first_reading_mins)

    second_wpm = 200
    second_reading_mins = 2
    actual = diary.reading_chunk(second_wpm, second_reading_mins)
    expected = "Sunday: " + "Sleep " + ("sleep " * 398).strip()
    assert actual == expected


def test_diary_entry_empty_string():
    with pytest.raises(Exception) as error:
        DiaryEntry("", "")
    assert str(error.value) == "Diary entries must have a title or contents"
