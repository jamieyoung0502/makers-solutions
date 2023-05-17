from lib.task_list import TaskList
from unittest.mock import Mock

"""
When I first init a task list
There are no tasks
And none are complete
"""

def test_task_list_initially_empty_and_incomplete():
    task_list = TaskList()
    assert task_list.all() == []
    assert task_list.all_complete() == False

"""
When I add a task or tasks to my task list
I see those instances in my task list
"""

def test_task_list_add_fake_tasks():
    list= TaskList()
    fake_task = Mock()
    list.add(fake_task)
    assert list.all() == [fake_task]

    fake_task_2 = Mock()
    list.add(fake_task_2)
    assert list.all() == [fake_task, fake_task_2]


"""
When I add a task or tasks to my task list
The status of all tasks is initially set to False
When I mark them as complete
All tasks are marked as complete
"""

def test_task_list_all_tasks_init_to_false():
    list= TaskList()
    fake_task_1 = Mock()
    fake_task_1.is_complete.return_value = False
    list.add(fake_task_1)
    assert list.all_complete() == False

    fake_task_2 = Mock()
    fake_task_1.is_complete.return_value = True
    fake_task_2.is_complete.return_value = True
    list.add(fake_task_2)
    assert list.all_complete() == True
