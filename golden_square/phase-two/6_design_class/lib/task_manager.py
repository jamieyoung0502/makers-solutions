from datetime import datetime


class TaskManager:
    def __init__(self):
        self._tasks = {}

    def add_task(self, task):
        if task:
            self._tasks.update({task: {"status": False, "created": datetime.utcnow()}})

    def list_tasks(self, completed=False):
        if completed:
            tasks_todo = [
                task for task in self._tasks if self._tasks[task]["status"] == True
            ]
        else:
            tasks_todo = [
                task for task in self._tasks if self._tasks[task]["status"] == False
            ]

        sorted_tasks_todo = sorted(
            tasks_todo, key=lambda task: self._tasks[task]["created"], reverse=True
        )

        return sorted_tasks_todo

    def complete_task(self, task):
        self._tasks[task]["status"] = True


# alternative for list_tasks
# return list(
#     filter(
#         lambda task: (self._tasks[task]["status"] == False), self._tasks.keys()
#     )
# )
