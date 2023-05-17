from lib.cohort import Cohort
from lib.student import Student

class CohortRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def find_with_students(self, student_id):
        query = """
        SELECT
            cohorts.id AS cohort_id,
            cohorts.name AS cohort_name,
            cohorts.starting_date,
            students.id AS student_id,
            students.name AS student_name
        FROM
            students
            JOIN cohorts ON cohorts.id = students.cohort_id
        WHERE
            cohorts.id = %s;
        """
        rows = self._connection.execute(query, [student_id])

        students = [Student(row["student_id"], row["student_name"], row["cohort_id"])  for row in rows]

        return Cohort(rows[0]["cohort_id"], rows[0]["cohort_name"], rows[0]["starting_date"], students)
