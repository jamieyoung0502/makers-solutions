# Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user <br>
> So that I can manage my time <br>
> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def estimate_reading_time(text: str) -> str:
    # Parameters:
    #   text: string containing words
    #   e.g. "hello world"
    # Returns:
    #   string: estimated number of minutes for how long it would take to read the text
    #   e.g. "93 minutes"
    pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
for an empty string
return zero
"""
def test_empty_string():
    estimate_reading_time("")
    # => "0 minute read"

"""
for text less with than 200 words
return less than a minute
"""
def test_text_with_less_than_200_words():
    estimate_reading_time("hello world")
    # => "less than a minute's read"

"""
for text with 1000 words
return 5 minutes
"""
def test_text_with_1000_words():
    estimate_reading_time("hello " * 1000).strip()
    # => "5 minute read"

"""
for text with 20000 words
return 1 hour and 40 minutes
"""
def test_text_with_20000_words():
    estimate_reading_time("hello " * 20000).strip()
    # => "1 hour 40 minute read"

"""
for text with 350 words (round up)
return 2 minute read
"""
def test_text_with_350_words():
    estimate_reading_time("hello " * 350).strip()
    # => "2 minute read"

"""
for text with 250 words (round up)
return 2 minute read
"""
def test_text_with_250_words():
    estimate_reading_time("hello " * 250).strip()
    # => "2 minute read"

"""
for text with 1000 words separated by touching commas
return 5 minutes
"""
def test_text_with_1000_words_and_commas():
    estimate_reading_time("hello," * 1000).strip()
    # => "5 minute read"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python
# EXAMPLE
```

Ensure all test function names are unique, otherwise pytest will ignore them!
