from lib.diary_entry import DiaryEntry
from lib.diary_entry_numbers import DiaryEntryNumbers
from lib.task import Task

class Diary:
    def __init__(self):
        self.tasks = []
        self.numbers = set([])
        self.entries = []

    def add_item(self, item):
        if isinstance(item, Task):
            self.tasks.append(item.task)
        elif isinstance(item, DiaryEntryNumbers):
            # for num in item.numbers:
            #     if num not in self.numbers:
            #         self.numbers += item.numbers
            self.numbers.update(item.numbers)
        elif isinstance(item, DiaryEntry):
            self.entries.append(item)
        else:
            raise ValueError("Invalid item type")

    def list_item(self, item):
        if item == "tasks":
            return self.tasks
        elif item == "numbers":
            return list(self.numbers)
        elif item == "entries":
            return self.entries
        else:
            raise ValueError("Invalid item type")

    def suggest_entry(self, minutes, wpm):
        if not self.entries:
            return None
        max_words = minutes * wpm
        return [entry for entry in self.entries if entry.length == max_words]