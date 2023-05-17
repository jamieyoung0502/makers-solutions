
from lib.post import Post
from unittest.mock import Mock

"""
Creates an instance of Post
"""
def test_recipe_constructs():
    user = Mock()
    user.id.return_value = 1

    post = Post(1, 'post title', 'post content', 1, user.id())
    assert post.id == 1
    assert post.title == "post title"
    assert post.content == "post content"
    assert post.views == 1
    assert post.user_id == 1

"""
We can format posts to look nice
"""
def test_posts_format_nicely():
    user = Mock()
    user.id.return_value = 1
    post = Post(1, 'post title', 'post content', 1, user.id())
    assert str(post) == "Post(id=1, title='post title', content='post content', views=1, user_id=1)"

"""
We can compare two identical posts
And have them be equal
"""
def test_two_posts_are_equal():
    user = Mock()
    user.id.return_value = 1

    post_1 = Post(1, 'post title', 'post content', 1, user.id())
    post_2 = Post(1, 'post title', 'post content', 1, user.id())
    assert post_1 == post_2
