import re, math


def estimate_reading_time(text: str) -> str:
    word_list = re.findall(r"[A-Za-z]+", text)
    length = len(word_list)

    if length == 0:
        return "0 minute read"
    if length < 200:
        return "less than a minute's read"

    length_rounded_up = math.ceil(length / 200) * 200
    num_minutes = math.ceil(length_rounded_up) // 200
    if num_minutes < 60:
        return f"{num_minutes} minute read"

    num_hours = num_minutes // 60
    num_minutes = abs((num_hours * 60) - num_minutes)
    return f"{num_hours} hour and {num_minutes} minute read"
