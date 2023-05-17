from lib.task_list import TaskList
from unittest.mock import Mock

def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

"""
When I add a task or tasks to my task list
I see those instances in my task list
"""
def test_task_list_add_fake_tasks():
    list= TaskList()
    fake_task = Mock()
    list.add(fake_task)
    assert list.tasks == [fake_task]

    fake_task_2 = Mock()
    list.add(fake_task_2)
    assert list.tasks == [fake_task, fake_task_2]

"""
When I add a task or tasks to my task list
The status of all tasks is initially set to False
"""
def test_task_list_all_tasks_init_to_false():
    list= TaskList()
    fake_task = Mock()
    fake_task.is_complete.return_value = False
    list.add(fake_task)
    assert list.all_complete() == False


"""
When I add a task or tasks to my task list and mark them as complete
All tasks are marked as complete
"""
def test_task_list_complete_all_tasks():
    list= TaskList()
    fake_task_1 = Mock()
    fake_task_1.is_complete.return_value = True
    list.add(fake_task_1)
    assert list.all_complete() == True

    fake_task_2 = Mock()
    fake_task_2.is_complete.return_value = False
    list.add(fake_task_2)
    assert list.all_complete() == False


