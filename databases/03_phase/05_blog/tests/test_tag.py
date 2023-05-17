
from lib.tag import Tag

"""
Creates an instance of comment
"""
def test_tag_constructs():
    tag = Tag(1, 'Python')
    assert tag.id == 1
    assert tag.name == "Python"

"""
We can format comments to look nice
"""
def test_tags_format_nicely():
    tag = Tag(1, 'Python')
    assert str(tag) == "Tag(id=1, name='Python')"

"""
We can compare two identical comments
And have them be equal
"""
def test_two_tags_are_equal():
    tag_1 = Tag(1, 'Python')
    tag_2 = Tag(1, 'Python')
    assert tag_1 == tag_2

