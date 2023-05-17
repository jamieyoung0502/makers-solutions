def make_snippet(string):
    if len(string) == 0:
        raise Exception("can't pass an empty string")

    word_list = string.split(" ")
    length = len(word_list)

    if length > 5:
        return " ".join(word_list[0:5]) + " ..."

    return string