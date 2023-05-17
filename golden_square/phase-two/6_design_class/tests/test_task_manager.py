from lib.task_manager import TaskManager

"""
Initially, there are no tasks
"""


def test_task_manager_test_no_tasks():
    task_manager = TaskManager()
    actual = task_manager.list_tasks()
    expected = []
    assert actual == expected


"""
When we try to add a task with no text
There are no tasks reflected in the task list
"""


def test_task_manager_empty_string_not_added_as_task():
    task_manager = TaskManager()
    task_manager.add_task("")
    actual = task_manager.list_tasks()
    expected = []
    assert actual == expected


"""
When we add two tasks with text
Each is reflected in the list of tasks to complete in reverse order
"""


def test_task_manager_add_two_tasks_to_todo_list():
    task_manager = TaskManager()
    task_manager.add_task("wash the dog")
    task_manager.add_task("wash the cat")
    actual = task_manager.list_tasks()
    expected = ["wash the cat", "wash the dog"]
    assert actual == expected


"""
When a task is marked as complete
It is removed from our lists of tasks to complete
"""


def test_task_manager_removes_task_when_completed():
    task_manager = TaskManager()
    task_manager.add_task("wash the dog")
    task_manager.add_task("wash the cat")
    task_manager.complete_task("wash the cat")
    actual = task_manager.list_tasks()
    expected = ["wash the dog"]
    assert actual == expected


"""
When passed a second argument of True
All completed tasks are returned
"""


def test_task_manager_removes_task_when_completed():
    task_manager = TaskManager()
    task_manager.add_task("wash the dog")
    task_manager.add_task("wash the cat")
    task_manager.complete_task("wash the cat")
    actual = task_manager.list_tasks(True)
    expected = ["wash the cat"]
    assert actual == expected
