
from lib.post import Post

"""
Creates an instance of post
"""
def test_post_constructs():
    post = Post(1, 'post title', 'post content', None)
    assert post.id == 1
    assert post.title == "post title"
    assert post.content == "post content"
    assert post.comments == None

"""
We can format posts to look nice
"""
def test_posts_format_nicely():
    post = Post(1, 'post title', 'post content', None)
    assert str(post) == "Post(id=1, title='post title', content='post content', comments=None)"

"""
We can compare two identical posts
And have them be equal
"""
def test_two_posts_are_equal():
    post_1 = Post(1, 'post title', 'post content', None)
    post_2 = Post(1, 'post title', 'post content', None)
    assert post_1 == post_2

