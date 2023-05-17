from lib.task import Task

def test_can_be_marked_as_complete():
    task = Task("Walk the dog")
    assert task.title == "Walk the dog"
    assert task.complete == False
    task.mark_complete()
    assert task.is_complete() == True
