import re
class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.length = len(contents.split())
        self.numbers = []

        self.__extract_numbers()

    def __extract_numbers(self):
        matches = re.findall(r"\b0\d{10}\b", self.contents)
        # \b word boundary anchor, matches the boundary between alpha char and a non-alpha char
        # 0 matches the literal character '0'
        # \d{10} matches any digit character 10 times in a row
        # \b ensures that the match ends with a digit

        if matches:
            for match in matches:
                self.numbers.append(match)

