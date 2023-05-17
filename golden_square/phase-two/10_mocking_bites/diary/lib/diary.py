class Diary:
    def __init__(self, contents):
        self._contents = contents

    def read(self):
        return self._contents