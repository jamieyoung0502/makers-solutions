### User stories

> As a user <br>
> So that I can record my experiences <br>
> I want to keep a regular diary

<br>

> As a user <br>
> So that I can reflect on my experiences <br>
> I want to read my past diary entries

<br>

> As a user <br>
> So that I can reflect on my experiences in my busy day <br>
> I want to select diary entries to read based on how much time I have and my reading speed

<br>

> As a user <br>
> So that I can keep track of my tasks <br>
> I want to keep a todo list along with my diary

<br>

> As a user <br>
> So that I can keep track of my numbers <br>
> I want to see a list of all of the mobile phone numbers in all my diary entries

### Design the Class System

```
                                        ┌────────────────────────────────────┐
                                        │ Diary                              │
                                        │                                    │
                                        │ - add_task(task)                   │
                                        │ - list_tasks()                     │
                                        │                                    │
                                        │ - add_number(numbers)              │
                                        │ - list_numbers()                   │
                                        │                                    │
                                        │ - add_entry(entry)                 │
                                        │ - read_entry(title)                │
                                        │ - suggest_entry(minutes, wpm)      │
                                        └────────────────┬───────────────────┘
                 │                                       │                                       │
                 │                                       │                                       │
                 ▼                                       ▼                                       ▼
                                              owns a list of ...

┌────────────────────────────────────┐ ┌────────────────────────────────────┐ ┌────────────────────────────────────┐
│ DiaryEntryNumbers                  │ │ Diary Entry                        │ │ Task                               │
│                                    │ │                                    │ │                                    │
│ - initialize(numbers)              │ │ - initialize(title, contents)      │ │ - initialize(title)                │
│ - numbers [property]               ◄─┤ - title [property]                 │ │ - task [property]                  │
│                                    │ │ - contents [property]              │ │  [property]                        │
│                                    │ │ - extract_numbers(entry)           │ │                                    │
└────────────────────────────────────┘ │ - numbers [property]               │ └────────────────────────────────────┘
                                       │                                    │
                                       └────────────────────────────────────┘
```

### Design the Interface of each Class

```python

# lib/diary.py
class Diary:
    # User-facing properities (i.e. self.)
    #   tasks: list of instances of Task
    #   numbers: list of phone numbers
    #   entries: list of DiaryEntry instances

    def __init__(self):
        pass # No code here yet

    # 1. do one of these for each class ...
    def add_task(self, task):
        # Parameters:
        #   task: an instance of Task
        # Side-effects:
        #   Adds the task to the tasks property of the self object
        pass # No code here yet

    # 2. or ...
    def add_item(self, item):
        # Parameters:
        #   item: an instance of either Task, DiaryEntryNumbers, or DiaryEntry
        # Side-effects:
        #   Adds the item to the corresponding property of the self object
        if isinstance(item, Task):
            self.tasks.append(item)
        elif isinstance(item, DiaryEntryNumbers):
            self.numbers.append(item)
        elif isinstance(item, DiaryEntry):
            self.entries.append(item)
        else:
            # value error is used for right type but inappropriate value
            raise ValueError("Invalid item type")

    # similarly (but a bit pointless if self.methods are public)
    def list_item(self, item):
        # Parameters:
        #   item: tasks, numbers or entries
        # Side-effects:
        #   Lists all instances of the item
        if item == "tasks":
            return self.tasks
        elif item == "numbers":
            return self.numbers
        elif item == "entries":
            return self.entries
        else:
            raise ValueError("Invalid item type")

    def suggest_entry(minutes, wpm):
        # Parameters:
        #   minutes: an integer of minutes the reader has to read
        #   wpm: an integer of words the reader can read per minute
        # Side-effects:
        #   Returns an instance of DiaryEntry that the user can read the most of (but not complete) given their time to read and wpm
        pass

# lib/task.py
class Task:
    # User-facing properities (i.e. self.)
    #   title: a string of the task
    def __init__(self, title):
        # Parameters:
        #   title: a string representing task to do
        # Side-effects: sets the title property
        pass # No code here yet

# lib/diary_entry_numbers.py
# this one feels a bit pointless given I'm including this information in DiaryEntry
class DiaryEntryNumbers:
    # User-facing properities (i.e. self.)
    #   numbers: a string representing phone number
    def __init__(self, numbers):
        # Parameters:
        #   numbers: a string representing phone numbers
        # Side-effects: sets the numbers property
        pass # No code here yet

# lib/diary_entry.py
class DiaryEntry:
    # User-facing properities (i.e. self.)
    #   title: a string of the title of a diary entry
    #   contents: a string of the contents of a diary entry
    #   numbers: a string representing phone numbers
    #   or a list of DiaryEntryNumbers instances that are made as a result of phone numbers being included in the diary entry
    def __init__(self):
        # Parameters:
        #   title: a string of the title of a diary entry
        #   contents: a string of the contents of a diary entry
        #   numbers: a string representing mobile phone numbers
        # Side-effects: sets the title and contents properties; calls private method __extract_numbers which updates self.numbers on initialization
        pass # No code here yet

    def __extract_number()
        # Side-effects: extracts each phone number found in the diary entry and adds to self.numbers
```

### Examples of Integration Tests

```python

# adding and listing

"""
When I add multiple diary entries
I can see a list of all diary entries
"""

def test_diary_add_and_list_multiple_entries():
    diary = Diary()
    entry_1 = DiaryEntry("title", "contents")
    entry_2 = DiaryEntry("title", "contents")
    diary.add_item(entry_1)
    diary.add_item(entry_2)
    assert diary.list_item("entries") == [entry_1, entry_2]

"""
When I add multiple diary entries with phone numbers
I can see a list of phone numbers from all diary entries
"""

def test_diary_add_and_list_multiple_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("title", "contents with 07800000001")
    entry_2 = DiaryEntry("title", "contents with 07800000002")
    number_1 = DiaryEntryNumbers(entry_1.numbers)
    number_2 = DiaryEntryNumbers(entry_2.numbers)
    diary.add_item(number_1)
    diary.add_item(number_2)
    assert diary.list_item("numbers") == ["07800000001", "07800000002"]

"""
When I add multiple tasks to my diary
I can see a list of task instances
"""

def test_diary_add_and_list_multiple_tasks():
    diary = Diary()
    task_1 = Task("wash the dog")
    task_2 = Task("wash the cat")
    diary.add_item(task_1)
    diary.add_item(task_2)
    assert diary.list_item("tasks") == ["wash the dog", "wash the cat"]

```

### Examples of Unit Tests

```python
# lib/test_diary.py
"""
When no diary entries, numbers or tasks have been added
I see an empty list for each
"""

def test_diary_empty_entry_list_on_init():
    diary = Diary()
    assert diary.list_item("entries") == []

"""
When there are no diary entries
There are None entries to read
"""

def test_diary_when_empty_no_suggested_reading():
    diary = Diary()
    assert diary.reading_time() == None

# lib/test_diary_entry.py
"""
When I create a diary entry with a phone number
Any phone number is correctly extracted from the contents and saved to self.number
"""

def test_diary_entry_extracts_valid_number():
    entry = DiaryEntry("title", "contents with 07800000001")
    assert entry.number == ["07800000001"]

"""
When I create a diary entry with non-valid phone numbers
These numbers are not extracted from the diary entry
"""

def test_diary_entry_invalid_numbers_ignored():
    entry = DiaryEntry("title", "contents 123")
    assert entry.number == []

"""
When I create a diary entry with a phone number
It ignores invalid numbers and extracts valid number only
"""

def test_diary_entry_extracts_valid_ignores_invalid_numbers():
    entry = DiaryEntry("title", "contents with 123 07800000001")
    assert entry.number == ["07800000001"]

"""
When I create a diary entry with phone numbers that aren't unique
It ignores duplicate numbers
"""

def test_diary_entry_extracts_valid_number_ignores_duplicates():
    entry_1 = DiaryEntry("title", "contents with 123 07800000001 07800000001")
    entry_2 = DiaryEntry("title", "contents with 123 07800000001")
    assert entry.number == ["07800000001"]

"""
When I create a diary entry with two valid phone numbers
Both numbers are added
"""

def test_diary_entry_extracts_two_valid_numbers():
    entry_1 = DiaryEntry("title", "contents with 123 07800000001 07800000002")
    assert entry_1.numbers == ["07800000001", "07800000002"]

# if time, add edge cases for +44

```
