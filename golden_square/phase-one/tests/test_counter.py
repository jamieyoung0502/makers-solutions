from lib.counter import Counter

"""
reports zero initially
"""


def test_counter_initally_reports_zero():
    counter = Counter()
    count = counter.report()
    assert count == "Counted to 0 so far."


"""
when number is added, count is reflected in final count
"""


def test_counter_tracks_and_returns_no_of_counts():
    counter = Counter()
    counter.add(1)
    count = counter.report()
    assert count == "Counted to 1 so far."


"""
can call add method multiple times
"""


def test_counter_tracks_multiple_counts():
    counter = Counter()
    for index in range(5):
        counter.add(1)
    count = counter.report()
    assert count == "Counted to 5 so far."
