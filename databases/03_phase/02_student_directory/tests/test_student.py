
from lib.student import Student
from unittest.mock import Mock

"""
Creates an instance of student
"""
def test_student_constructs():
    cohort = Mock()
    cohort.id.return_value = 1
    student = Student(1, 'Adrian', cohort.id())
    assert student.id == 1
    assert student.name == "Adrian"
    assert student.cohort_id == 1


"""
We can format students to look nice
"""
def test_students_format_nicely():
    cohort = Mock()
    cohort.id.return_value = 1
    student = Student(1, 'Adrian', cohort.id())
    assert str(student) == "Student(id=1, name='Adrian', cohort_id=1)"

"""
We can compare two identical students
And have them be equal
"""
def test_two_students_are_equal():
    cohort = Mock()
    cohort.id.return_value = 1
    student_1 = Student(1, 'Adrian', cohort.id())
    student_2 = Student(1, 'Adrian', cohort.id())
    assert student_1 == student_2

