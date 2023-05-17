class TaskFormatter:
    def __init__(self, task): # task is an instance of Task
        self._task = task

    def format(self):
        return f"- {'[x]' if self._task.is_complete() else '[ ]'} {self._task.title}"