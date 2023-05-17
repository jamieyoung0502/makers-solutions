
from lib.post import Post

"""
Creates an instance of post
"""
def test_post_constructs():
    post = Post(1, 'post title')
    assert post.id == 1
    assert post.title == "post title"

"""
We can format posts to look nice
"""
def test_posts_format_nicely():
    post = Post(1, 'post title')
    assert str(post) == "Post(id=1, title='post title')"

"""
We can compare two identical posts
And have them be equal
"""
def test_two_posts_are_equal():
    post_1 = Post(1, 'post title')
    post_2 = Post(1, 'post title')
    assert post_1 == post_2

