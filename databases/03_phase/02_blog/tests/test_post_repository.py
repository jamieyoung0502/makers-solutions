from lib.post_repository import PostRepository
from lib.post import Post
from lib.comment import Comment

def test_find_with_comments(db_connection):
    db_connection.seed("seeds/blog.sql")
    repository = PostRepository(db_connection)
    post = repository.find_with_comments(1)

    assert post == Post(1, 'post title', 'post content', [
        Comment(1, 'Adrian', 'great post', 1),
        Comment(2, 'Nish', 'crap post', 1),
    ])

