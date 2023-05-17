from lib.user_repository import UserRepository
from lib.user import User

"""
When we call UserRepository#all
We get a list of User objects reflecting the seed data.
"""
def test_all_users(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    users = repository.all()

    assert users == [
        User(1, 'adrian', 'adrian@gmail.com')
    ]

"""
When we call UserRepository#find
We get a single User object reflecting the seed data.
"""

def test_find_specific_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    user = repository.find(1)
    assert user == User(1, 'adrian', 'adrian@gmail.com')


"""
When we call UserRepository#create
We get a new record in the database.
"""
def test_create_new_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None, 'paul', 'paul@gmail.com'))

    users = repository.all()
    assert users == [
        User(1, 'adrian', 'adrian@gmail.com'),
        User(2, 'paul', 'paul@gmail.com')
    ]

"""
When we call UserRepository#update
We update a record in the database.
"""
def test_update_a_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None, 'paul', 'paul@gmail.com'))
    repository.update("username", "pgibson", 2)

    users = repository.all()
    assert users == [
        User(1, 'adrian', 'adrian@gmail.com'),
        User(2, 'pgibson', 'paul@gmail.com')
    ]

"""
When we call UserRepository#delete
We remove a record from the database.
"""

def test_delete_a_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None, 'paul', 'paul@gmail.com'))

    users = repository.all()
    assert users == [
        User(1, 'adrian', 'adrian@gmail.com'),
        User(2, 'paul', 'paul@gmail.com')
    ]

    repository.delete(2)
    users = repository.all()
    assert users == [
        User(1, 'adrian', 'adrian@gmail.com'),
    ]