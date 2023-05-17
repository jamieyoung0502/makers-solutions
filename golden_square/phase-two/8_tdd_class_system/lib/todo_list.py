class TodoList:
    def __init__(self):
        self._task_list = []

    def add(self, todo):
        self._task_list.append(todo)
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos


    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return [task for task in self._task_list if task.status == False]

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return [task for task in self._task_list if task.status == True]

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        incomplete = self.incomplete()
        for task in incomplete:
            task.status = True