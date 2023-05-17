from lib.check_codeword import check_codeword


"""
If codeword is correct
Returns 'Correct! Come in.
"""


def test_check_codeword_returns_correct_for_horse():
    answer = check_codeword("horse")
    assert answer == "Correct! Come in."


"""
if codeword has correct first word but wrong last letter
Returns 'WRONG!'
"""


def test_check_codeword_with_correct_first_incorrect_last():
    answer = check_codeword("hat")
    assert answer == "WRONG!"


"""
if codeword has incorrect first word but correct last letter
Returns 'WRONG!'
"""


def test_check_codeword_with_incorrect_first_correct_last():
    answer = check_codeword("rate")
    assert answer == "WRONG!"


"""
If codeword is close but not correct
Returns 'Close, but nope.'
"""


def test_check_codeword_returns_close_for_home():
    answer = check_codeword("home")
    assert answer == "Close, but nope."


"""
If codeword is not even close
Return 'WRONG!'
"""


def test_check_codeword_returns_wrong_for_everything_else():
    answer = check_codeword("password")
    assert answer == "WRONG!"
