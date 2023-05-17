class TaskList:
    def __init__(self):
        self._tasks = []

    def add(self, task):
        self._tasks.append(task)

    def all(self):
        return self._tasks

    def all_complete(self):
        if len(self._tasks) == 0:
            return False
        return all([task.is_complete() for task in self._tasks])

