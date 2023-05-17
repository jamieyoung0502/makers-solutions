class GrammarStats:
    def __init__(self):
        self._no_of_checks = 0
        self._no_passed = 0

    def check(self, text):
        if text == "":
            raise Exception("cannot check an empty string")

        self._no_of_checks += 1
        outcome = text[0] == text[0].capitalize() and text[-1] in "!.?"
        self._no_passed += 1 if outcome else 0

        return outcome

    def percentage_good(self):
        if self._no_of_checks == 0 or self._no_passed == 0:
            return 0

        percentage = 100 * float(self._no_passed) // float(self._no_of_checks)
        return round(percentage)
