import pytest
from lib.grammar_stats import GrammarStats

"""
if checking grammar of an empty string
raise custom error
"""


def test_grammar_stats_empty_string():
    stats = GrammarStats()

    with pytest.raises(Exception) as error:
        stats.check("")
    assert str(error.value) == "cannot check an empty string"


"""
if checking grammar of a string that starts with capital but has no punctuation
return False
"""


def test_grammar_stats_check_capital_no_punc():
    stats = GrammarStats()
    actual = stats.check("This is not correct")
    expected = False
    assert actual == expected


"""
if checking grammar of a string that does not starts with capital but has punctuation
return False
"""


def test_grammar_stats_check_punc_no_capital():
    stats = GrammarStats()
    actual = stats.check("this is not correct.")
    expected = False
    assert actual == expected


"""
if checking grammar of a string that starts with capital and has punctuation
return True
"""


def test_grammar_stats_check_capital_and_punc():
    stats = GrammarStats()
    actual = stats.check("This is correct.")
    expected = True
    assert actual == expected


"""
if one check passed and one failed
return 50
"""


def test_grammar_stats_percentage_returns_int():
    stats = GrammarStats()
    stats.check("This is correct.")
    stats.check("This is wrong")
    result = stats.percentage_good()

    assert isinstance(result, int)


"""
if 6 checks passed and 3 failed
return 66
"""


def test_grammar_stats_percentage():
    stats = GrammarStats()
    for num in range(0, 6):
        stats.check("This is correct.")

    for num in range(0, 3):
        stats.check("This is wrong")

    actual = stats.percentage_good()
    expected = 66
    assert actual == expected


"""
if no checks have been made or no tests have passed
return 0
"""


def test_grammar_stats_percentage_if_all_fail():
    stats = GrammarStats()

    for num in range(0, 3):
        stats.check("This is wrong")

    actual = stats.percentage_good()
    expected = 0
    assert actual == expected

    new_stats = GrammarStats()
    actual = new_stats.percentage_good()
    expected = 0
    assert actual == expected
