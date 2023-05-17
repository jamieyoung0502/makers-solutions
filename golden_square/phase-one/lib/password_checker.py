class PasswordChecker:
    def check(self, password):
        if not isinstance(password, str):
            raise TypeError(f"Expected a string but got {type(password).__name__}")

        if len(password) >= 8:
            return True
        else:
            raise Exception("Invalid password, must be 8+ characters.")
