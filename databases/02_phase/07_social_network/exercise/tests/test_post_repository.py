from lib.post_repository import PostRepository
from lib.post import Post
from unittest.mock import Mock

"""
When we call PostRepository#all
We get a list of Post objects reflecting the seed data.
"""
def test_all_posts(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    posts = repository.all()

    assert posts == [
        Post(1, 'snakes, rubies and tdd', 'hello world', 1, 1)
    ]

"""
When we call PostRepository#find
We get a single Post object reflecting the seed data.
"""

def test_find_specific_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    post = repository.find(1)
    assert post == Post(1, 'snakes, rubies and tdd', 'hello world', 1, 1)


"""
When we call PostRepository#create
We get a new record in the database.
"""
def test_create_new_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    user = Mock()
    user.id.return_value = 1
    repository.create(Post(None, 'post title', 'post content', 1, user.id()))

    posts = repository.all()
    assert posts == [
        Post(1, 'snakes, rubies and tdd', 'hello world', 1, 1),
        Post(2, 'post title', 'post content', 1, user.id())
    ]

"""
When we call PostRepository#update
We update a record in the database.
"""
def test_update_a_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    user = Mock()
    user.id.return_value = 1
    repository.create(Post(None, 'post title', 'post content', 1, user.id()))
    repository.update("title", "better title", 2)

    users = repository.all()
    assert users == [
        Post(1, 'snakes, rubies and tdd', 'hello world', 1, 1),
        Post(2, 'better title', 'post content', 1, user.id())
    ]

"""
When we call PostRepository#delete
We remove a record from the database.
"""

def test_delete_a_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    user = Mock()
    user.id.return_value = 1
    repository.create(Post(None, 'post title', 'post content', 1, user.id()))

    posts = repository.all()
    assert posts == [
        Post(1, 'snakes, rubies and tdd', 'hello world', 1, 1),
        Post(2, 'post title', 'post content', 1, user.id())
    ]

    repository.delete(2)
    posts = repository.all()
    assert posts == [
        Post(1, 'snakes, rubies and tdd', 'hello world', 1, 1)
    ]