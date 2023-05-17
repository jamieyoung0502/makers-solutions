from lib.estimate_reading_time import estimate_reading_time

"""
for an empty string
return zero
"""


def test_empty_string():
    result = estimate_reading_time("")
    assert result == "0 minute read"


"""
for text less with than 200 words
return less than a minute
"""


def test_text_with_less_than_200_words():
    result = estimate_reading_time("hello world")
    assert result == "less than a minute's read"


"""
for text with 1000 words
return 5 minutes
"""


def test_text_with_1000_words():
    test_string = ("hello " * 1000).strip()
    result = estimate_reading_time(test_string)
    assert result == "5 minute read"


"""
for text with 20000 words
return 1 hour and 40 minutes
"""


def test_text_with_20000_words():
    test_string = ("hello " * 20000).strip()
    result = estimate_reading_time(test_string)
    assert result == "1 hour and 40 minute read"


"""
for text with 350 words (round up)
return 2 minute read
"""


def test_text_with_350_words():
    test_string = ("hello " * 350).strip()
    result = estimate_reading_time(test_string)
    assert result == "2 minute read"


"""
for text with 250 words (round up)
return 2 minute read
"""


def test_text_with_250_words():
    test_string = ("hello " * 250).strip()
    result = estimate_reading_time(test_string)
    assert result == "2 minute read"


"""
for text with 1000 words separated by touching commas
return 5 minutes
"""


def test_text_with_1000_words_and_commas():
    test_string = ("hello," * 1000).strip()
    result = estimate_reading_time(test_string)
    assert result == "5 minute read"
