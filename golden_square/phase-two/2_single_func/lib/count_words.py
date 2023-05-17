import re

def count_words(string):
    if not isinstance(string, str):
        raise TypeError(f"Expected a string but got {type(string).__name__}")

    word_list = re.findall(r'[A-Za-z]+', string)
    count = len(word_list)
    print(word_list)
    return count

