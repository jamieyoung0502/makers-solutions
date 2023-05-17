class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary entries must have a title or contents")

        self._title = title
        self._contents = contents
        self._position = 0

    def format(self):
        # .title() capitalizes both words
        title = self._title.capitalize()
        contents = self._contents.capitalize()
        spacer = ": "
        full_stop = "" if contents[-1] == "." else "."

        return title + spacer + contents + full_stop

    def count_words(self):
        words = self.format()
        count = sum(1 for word in words.split(" "))
        return count

    def reading_time(self, wpm):
        count = self.count_words()
        return count // wpm

    def reading_chunk(self, wpm, minutes):
        read_up_to_index = (minutes * wpm) + self._position
        entry = self.format()
        entry_as_list = entry.split(" ")
        last_index = len(entry_as_list) - 1
        chunk = " ".join(entry_as_list[self._position : read_up_to_index])

        self._position = read_up_to_index + 1
        if self._position >= last_index:
            self._position = 0

        return chunk
