def make_snipper(string):
    if not isinstance(string, str):
        raise TypeError(f"Expected a string but got {type(string).__name__}")

    string_list = string.split(' ')
    result = f'{string_list[0]}'

    for index in range(1, len(string_list)):
        if index == 5:
            result += '...'
            break
        else:
            result += f' {string_list[index]}'
    return result

    # for index, word in enumerate(string_list, 1):