from lib.task_list import TaskList
from lib.task_formatter import TaskFormatter
from lib.task import Task

"""
Add multiple tasks
Tasks are not complete by default
"""

def test_adds_tasks_to_list():
    task_list = TaskList()
    task_1, task_2 = Task("Walk the dog"), Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_1.is_complete() == False and task_2.is_complete() == False
    assert task_list.all() == [task_1, task_2]


"""
Add multiple tasks
Tasks are not complete by default
When marked as complete
All are marked as completed
"""

def test_marks_tasks_as_complete():
    task_list = TaskList()
    task_1, task_2 = Task("Walk the dog"), Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_1.is_complete() == False and task_2.is_complete() == False

    task_1.mark_complete()
    task_2.mark_complete()
    assert task_1.is_complete() == True and task_2.is_complete() == True
    assert task_list.all_complete() == True

"""
Add two tasks
Tasks are not complete by default
Mark one as complete
Formatter indicates one has been completed, the other incomplete
When all marked as complete
Formatter indicates all tasks have been completed
"""

def test_marks_tasks_as_complete():
    task_list = TaskList()
    task_1, task_2 = Task("Walk the dog"), Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_1.is_complete() == False and task_2.is_complete() == False

    task_1.mark_complete()
    assert task_1.is_complete() == True and task_2.is_complete() == False

    task_1_formatted = TaskFormatter(task_1).format()
    task_2_formatted = TaskFormatter(task_2).format()
    assert task_1_formatted == "- [x] Walk the dog"
    assert task_2_formatted == "- [ ] Walk the cat"

    assert task_list.all_complete() == False
    task_2.mark_complete()
    assert task_list.all_complete() == True

    task_1_formatted = TaskFormatter(task_1).format()
    task_2_formatted = TaskFormatter(task_2).format()
    assert task_1_formatted == "- [x] Walk the dog"
    assert task_2_formatted == "- [x] Walk the cat"