from lib.cohort_repository import CohortRepository
from lib.student import Student
from lib.cohort import Cohort
from datetime import datetime

def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory.sql")
    repository = CohortRepository(db_connection)
    cohort = repository.find_with_students(1)

    starting_date = datetime.strptime('01/04/2023', '%d/%m/%Y').date()

    assert cohort == Cohort(1, 'April', starting_date, [
        Student(1, 'Adrian', 1),
        Student(2, 'Nish', 1),
        Student(3, 'Jasmine', 1),
        Student(4, 'Saamiya', 1)
    ])

