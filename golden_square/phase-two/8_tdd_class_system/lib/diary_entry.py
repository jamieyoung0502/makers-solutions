class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        if title == "" or contents == "":
            raise Exception("Diary entries must have a title or contents")

        self.title = title
        self.contents = contents
        self._contents_as_list = contents.split(" ")
        self._position = 0

    def count_words(self):
        words = self.contents
        count = sum(1 for word in words.split(" "))
        return count

    def reading_time(self, wpm):
        count = self.count_words()
        return count // wpm

    def reading_chunk(self, wpm, minutes):
        read_up_to_index = (minutes * wpm) + self._position
        last_index = len(self._contents_as_list) - 1
        chunk = " ".join(self._contents_as_list[self._position : read_up_to_index])

        self._position = read_up_to_index + 1
        if self._position >= last_index:
            self._position = 0

        return chunk

