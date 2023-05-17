
from lib.post_tag import PostTag

"""
Creates an instance of comment
"""
def test_post_tag_constructs():
    post_tag = PostTag(1, 1, 1)
    assert post_tag.id == 1
    assert post_tag.post_id == 1
    assert post_tag.tag_id == 1

"""
We can format comments to look nice
"""
def test_post_tags_format_nicely():
    post_tag = PostTag(1, 1, 1)
    assert str(post_tag) == "PostTag(id=1, post_id=1, tag_id=1)"

"""
We can compare two identical comments
And have them be equal
"""
def test_two_post_tags_are_equal():
    post_tag_1 = PostTag(1, 1, 1)
    post_tag_2 = PostTag(1, 1, 1)
    assert post_tag_1 == post_tag_2

