from lib.todo import Todo
from lib.todo_list import TodoList

"""
When add three tasks
All tasks are initially set to False
"""

def test_add_and_list_three_tasks_all_complete():
    todo_list = TodoList()
    task_1 = Todo("wash the dishes")
    task_2 = Todo("wash the dog")
    task_3 = Todo("wash the house")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)

    assert todo_list.incomplete() == [task_1, task_2, task_3]



"""
When I add three tasks to the list and mark two as complete
I see only the one incomplete task in a list
"""

def test_add_and_list_three_tasks_one_incomplete():
    todo_list = TodoList()
    task_1 = Todo("wash the dishes")
    task_2 = Todo("wash the dog")
    task_3 = Todo("wash the house")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    task_1.mark_complete()
    task_2.mark_complete()
    # assert todo_list.incomplete() == task_1 | task_2
    assert todo_list.incomplete() == [task_3]



"""
When I add three tasks to the list and mark two as complete
I see only the two completed tasks in a list
"""

def test_add_and_list_three_tasks_two_complete():
    todo_list = TodoList()
    task_1 = Todo("wash the dishes")
    task_2 = Todo("wash the dog")
    task_3 = Todo("wash the house")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    task_1.mark_complete()
    task_2.mark_complete()

    assert todo_list.complete() == [task_1, task_2]


"""
When I give up
All tasks are marked as complete
"""

def test_add_and_list_three_tasks_all_complete():
    todo_list = TodoList()
    task_1 = Todo("wash the dishes")
    task_2 = Todo("wash the dog")
    task_3 = Todo("wash the house")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    todo_list.give_up()

    assert todo_list.complete() == [task_1, task_2, task_3]


"""
When I give up
There should be no tasks marked as incomplete
"""

def test_add_and_list_three_tasks_none_incomplete():
    todo_list = TodoList()
    task_1 = Todo("wash the dishes")
    task_2 = Todo("wash the dog")
    task_3 = Todo("wash the house")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    todo_list.give_up()

    assert todo_list.incomplete() == []
