# File: lib/letter_counter.py

class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 0
        for char in self.text:
            if counter.get(char) or not char.isalpha():
                continue
            counter[char] = counter.get(char, self.text.count(char))
            if counter[char] > most_common_count:
                most_common = char
                most_common_count = counter[char]
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]