class SecretDiary:
    def __init__(self, diary):
        self._diary = diary
        self._locked = True

    def read(self):
        if self._locked:
            raise Exception("Go away!")
        return self._diary.read()

    def lock(self):
        self._locked = True

    def unlock(self):
        self._locked = False