from lib.string_builder import StringBuilder


def test_string_builder_returns_an_empty_string_if_empty():
    string_builder = StringBuilder()
    string_builder.add("")
    instance_string = string_builder.output()
    assert instance_string == ""

# can get rid of simpler tests if more complex ones cover them
# def test_string_builder_returns_length_of_string():
#     string_builder = StringBuilder()
#     string_builder.add("string")
#     length = string_builder.size()
#     assert length == len("string")


# def test_string_builder_returns_instance_string():
#     string_builder = StringBuilder()
#     string_builder.add("string")
#     instance_string = string_builder.output()
#     assert instance_string == "string"


"""
don't forget to test the behaviour as well; it's a string builder, not a setter
"""


def test_string_builder_combines_strings():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add("world")
    instance_string = string_builder.output()
    assert instance_string == "helloworld"


def test_string_builder_returns_length_of_combined_strings():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add("world")
    length = string_builder.size()
    assert length == len("helloworld")
