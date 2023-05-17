
from lib.user import User

"""
Creates an instance of User
"""
def test_recipe_constructs():
    user = User(1, 'user', 'user@gmail.com')
    assert user.id == 1
    assert user.username == "user"
    assert user.email_address == "user@gmail.com"


"""
We can format users to look nice
"""
def test_users_format_nicely():
    user = User(1, 'user', 'user@gmail.com')
    assert str(user) == "User(id=1, username='user', email_address='user@gmail.com')"

"""
We can compare two identical users
And have them be equal
"""
def test_two_users_are_equal():
    user_1 = User(1, 'user', 'user@gmail.com')
    user_2 = User(1, 'user', 'user@gmail.com')
    assert user_1 == user_2

