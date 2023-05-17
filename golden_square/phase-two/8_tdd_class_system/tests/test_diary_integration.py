from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
When I add two diary entries
I see them in a list
"""

def test_add_and_list_two_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("title", "contents")
    entry_2 = DiaryEntry("title", "contents")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

"""
When I add two diary entries
I can see the combined number of words from their contents
"""

def test_count_of_two_diary_entries_combined():
    diary = Diary()
    entry_1 = DiaryEntry("title", "contents")
    entry_2 = DiaryEntry("title", "contents")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 2

"""
When I add two diary entries
I can see the combined time it would take for me to read their contents
"""

def test_reading_time_for_two_diary_entries_combined():
    diary = Diary()
    entry_1 = DiaryEntry("title", "contents")
    entry_2 = DiaryEntry("title", "contents")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(1) == 2


"""
When I add two diary entries
I can see which entry I should read given my wpm and time I have to read
"""

def test_reading_time_for_two_diary_entries_combined():
    diary = Diary()
    entry_1 = DiaryEntry("title", "contents contents contents")
    entry_2 = DiaryEntry("title", "contents")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(1, 1) == entry_2