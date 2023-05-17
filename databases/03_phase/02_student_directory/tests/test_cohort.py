
from lib.cohort import Cohort

"""
Creates an instance of Cohort
"""
def test_cohort_constructs():
    cohort = Cohort(1, 'April', '01/04/2023', None)
    assert cohort.id == 1
    assert cohort.name == "April"
    assert cohort.starting_date == "01/04/2023"
    assert cohort.student_body == None


"""
We can format cohorts to look nice
"""
def test_cohorts_format_nicely():
    cohort = Cohort(1, 'April', '01/04/2023', None)
    assert str(cohort) == "Cohort(id=1, name='April', starting_date='01/04/2023', student_body=None)"

"""
We can compare two identical cohorts
And have them be equal
"""
def test_two_cohorts_are_equal():
    cohort_1 = Cohort(1, 'April', '01/04/2023', None)
    cohort_2 = Cohort(1, 'April', '01/04/2023', None)
    assert cohort_1 == cohort_2

