from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.diary_entry_numbers import DiaryEntryNumbers
from lib.task import Task

"""
When I add multiple diary entries
I can see a list of all diary entry instances
"""

def test_diary_add_and_list_multiple_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("title", "contents")
    entry_2 = DiaryEntry("title", "contents")
    diary.add_item(entry_1)
    diary.add_item(entry_2)
    assert diary.list_item("entries") == [entry_1, entry_2]

"""
When I add multiple tasks to my diary
I can see a list of the tasks I need to do
"""

def test_diary_add_and_list_multiple_tasks():
    diary = Diary()
    task_1 = Task("wash the dog")
    task_2 = Task("wash the cat")
    diary.add_item(task_1)
    diary.add_item(task_2)
    assert diary.list_item("tasks") == ["wash the dog", "wash the cat"]


"""
When I add a diary entry with a phone number
I can see that phone number
"""

def test_diary_add_single_entry_list_single_number():
    diary = Diary()
    entry_1 = DiaryEntry("title", "contents with 07800000001")
    number_1 = DiaryEntryNumbers(entry_1.numbers)
    diary.add_item(number_1)
    assert diary.list_item("numbers") == ["07800000001"]


"""
When I add multiple diary entries with unique phone numbers
I can see a list of phone numbers from both diary entries
"""

def test_diary_add_multiple_entries_list_multiple_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("title", "contents with 07800000001")
    entry_2 = DiaryEntry("title", "contents with 07800000002")
    number_1 = DiaryEntryNumbers(entry_1.numbers)
    number_2 = DiaryEntryNumbers(entry_2.numbers)
    diary.add_item(number_1)
    diary.add_item(number_2)
    assert ("07800000001" and "07800000002" in diary.list_item("numbers"))

"""
When I add a single entry with two unique numbers
I can see a list with both phone numbers
"""

def test_diary_add_single_entry_list_multiple_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("title", "contents with 07800000001 07800000002")
    number_1 = DiaryEntryNumbers(entry_1.numbers)
    diary.add_item(number_1)
    assert ("07800000001" and "07800000002" in diary.list_item("numbers"))


"""
When I create a multiple diary entries with multiple phone numbers that aren't unique
It ignores duplicate numbers
"""

def test_diary_add_multiple_entries_ignore_duplicate_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("title", "contents with 07800000001")
    entry_2 = DiaryEntry("title", "contents with 07800000001")
    number_1 = DiaryEntryNumbers(entry_1.numbers)
    number_2 = DiaryEntryNumbers(entry_2.numbers)
    diary.add_item(number_1)
    diary.add_item(number_2)
    assert diary.list_item("numbers") == ["07800000001"]

"""
When I want some suggested reading
Returns the instance of a diary entry that matches what I can read given the time I have and my wpm
"""

def test_diary_suggests_optimal_entry():
    diary = Diary()
    entry_1 = DiaryEntry("title", "contents and contents")
    entry_2 = DiaryEntry("title", "contents")
    diary.add_item(entry_1)
    diary.add_item(entry_2)
    assert diary.suggest_entry(1, 1) == [entry_2]

# there's room for a lot of expansion with suggested entry, however, I feel as though I did a lot of this
# in the previous chapter so I will be omitting it here