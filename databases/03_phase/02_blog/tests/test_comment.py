
from lib.comment import Comment
from unittest.mock import Mock

"""
Creates an instance of comment
"""
def test_comment_constructs():
    cohort = Mock()
    cohort.id.return_value = 1
    comment = Comment(1, 'Adrian', 'great post', cohort.id())
    assert comment.id == 1
    assert comment.name == "Adrian"
    assert comment.content == 'great post'
    assert comment.post_id == 1


"""
We can format comments to look nice
"""
def test_comments_format_nicely():
    cohort = Mock()
    cohort.id.return_value = 1
    comment = Comment(1, 'Adrian', 'great post', cohort.id())
    assert str(comment) == "Comment(id=1, name='Adrian', content='great post', post_id=1)"

"""
We can compare two identical comments
And have them be equal
"""
def test_two_comments_are_equal():
    cohort = Mock()
    cohort.id.return_value = 1
    comment_1 = Comment(1, 'Adrian', 'great post', cohort.id())
    comment_2 = Comment(1, 'Adrian', 'great post', cohort.id())
    assert comment_1 == comment_2

