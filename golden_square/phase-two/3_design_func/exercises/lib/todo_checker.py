def todo_checker(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError(f"Expected a string but got {type(text).__name__}")

    if "#TODO" in text:
        return True

    return False