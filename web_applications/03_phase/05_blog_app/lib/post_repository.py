from lib.post import Post


class PostRepository:
    def __init__(self):
        self.store = []
        self.length = 0

    def all(self):
        return self.store

    def all_by_tag(self, tag):
        return [post for post in self.store if tag in post.tags]

    def create(self, post):
        post.id = self._generate_next_id()
        self.store.append(post)
        self.length += 1
        return post

    def _generate_next_id(self):
        if not self.length:
            return 1
        return self.length + 1
