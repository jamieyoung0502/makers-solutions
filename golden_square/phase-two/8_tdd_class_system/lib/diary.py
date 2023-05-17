class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)

    def all(self):
        return self._entries

    def count_words(self):
        count = 0
        for entry in self._entries:
            count += entry.count_words()
        return count

    def reading_time(self, wpm):
        reading_time = 0
        for entry in self._entries:
            reading_time += entry.reading_time(wpm)
        return reading_time

    def find_best_entry_for_reading_time(self, wpm, minutes):
        read_up_to_index = minutes * wpm
        entry_reading_time_diff = []

        for entry in self._entries:
            last_index = len(entry._contents_as_list)
            diff = last_index - read_up_to_index
            entry_reading_time_diff.append((entry, diff))

        entry_reading_time_diff = sorted(entry_reading_time_diff, key=lambda pair: pair[1])

        for i in range(len(entry_reading_time_diff)):
            if entry_reading_time_diff[i][1] < 0:
                entry_reading_time_diff.append(entry_reading_time_diff.pop(i))

        return entry_reading_time_diff[0][0]

