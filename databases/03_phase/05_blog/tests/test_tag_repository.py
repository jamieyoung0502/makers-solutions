from lib.tag_repository import TagRepository
from lib.tag import Tag

def test_find_by_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = TagRepository(db_connection)
    tags = repository.find_with_tag('My weekend in Edinburgh')

    assert tags == [
        Tag(2, 'travel'),
    ]

