## Describe the Problem

> As a user
> So that I can keep track of my tasks
> I want a program that I can add todo tasks to and see a list of them.

> As a user
> So that I can focus on tasks to complete
> I want to mark tasks as complete and have them disappear from the list.

## Design the Class Interface

```python
class TaskManager:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   tasks: dictionary (task: status)
        # Side effects:
        #   Creates a dictionary associated with the object into which we will save a task (key) and its status (value)
        pass # No code here yet

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def list_tasks(self):
        # Returns:
        #   lists tasks marked as incomplete
        # Side-effects
        #   throws an error if no tasks have been added
        pass # No code here yet

    def complete_task(self, task):
        # Parameters:
        #   task: string representing a single task the user wants to make as complete
        # Returns:
        #   calls lists_tasks for updated list
        # Side-effects:
        #   changes the status of a task from False to True
        pass # No code here yet
```

## Example tests

```python

"""
Initially, there are no tasks
"""
task_manager = TaskManager()
task_manager.list_tasks() # => []


"""
When we try to add a task with no text
There are no tasks reflected in the task list
"""
task_manager = TaskManager()
task_manager.add_task("")
task_manager.list_tasks() # => []


"""
When we add two tasks with text
Each is reflected in the list of tasks to complete
"""
task_manager = TaskManager()
task_manager.add_task("wash the dog")
task_manager.add_task("wash the cat")
task_manager.list_tasks() # => ["wash the dog", "wash the cat"]


"""
When we complete a task
It is removed from our lists of tasks to complete
"""
task_manager = TaskManager()
task_manager.add_task("wash the dog")
task_manager.add_task("wash the cat")
task_manager.complete_task("wash the cat")
task_manager.list_tasks() # => ["wash the dog"]

# could do a nested dictionary to allow us to order by date
```
