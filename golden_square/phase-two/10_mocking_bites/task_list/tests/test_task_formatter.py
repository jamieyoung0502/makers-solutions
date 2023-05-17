from lib.task_formatter import TaskFormatter
from unittest.mock import Mock

"""
When I add a complete task to the formatter
and I format the task
it shows as being complete

When I add an incomplete task to the formatter
and I format the task
it shows as being incomplete
"""

def test_add_tasks_to_format():
    task_1, task_2 = Mock(), Mock()

    task_1.title, task_1.complete = "Walk the dog", True
    task_2.title, task_2.complete = "Walk the cat", False

    task_1.is_complete.return_value, task_2.is_complete.return_value = True, False

    formatter_1 = TaskFormatter(task_1)
    formatter_2 = TaskFormatter(task_2)

    task_1.is_complete.assert_not_called()
    task_2.is_complete.assert_not_called()

    assert formatter_1.format() == "- [x] Walk the dog"
    assert formatter_2.format() == "- [ ] Walk the cat"

    task_1.is_complete.assert_called()
    task_2.is_complete.assert_called()