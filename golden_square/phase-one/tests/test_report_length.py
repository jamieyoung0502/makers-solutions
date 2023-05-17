from lib.report_length import report_length

def test_report_length_gives_correct_length_of_str():
    length = report_length("abc")
    assert length == "This string was 3 characters long."


"""
when user inputs incorrect data type
returns e.g. object of type 'list' has no len()
"""
def test_report_length_gives_error_message_for_none_data_type():
    try:
        report_length(None)
    except TypeError as error:
        assert str(
            error) == f"object of type '{type(None).__name__}' has no len()"

# for use with isinstance
# def test_report_length_gives_error_message_for_list_data_type():
#     try:
#         report_length([1, 2, 3])
#     except TypeError as error:
#         assert str(error) == f"Expected a string but got {type([1, 2, 3]).__name__}"
