def grammar_checker(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError(f"Expected a string but got {type(text).__name__}")
    # pass in a tuple of the possible suffixes to check for
    if text and text.capitalize() == text and text.endswith(("!", "?", ".")):
        return True
    return False