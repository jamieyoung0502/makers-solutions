from lib.post_repository import PostRepository
from lib.post import Post

def test_find_by_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)
    posts = repository.find_with_tag_name('travel')

    assert posts == [
        Post(4, 'My weekend in Edinburgh'),
        Post(6, 'A foodie week in Spain')
    ]