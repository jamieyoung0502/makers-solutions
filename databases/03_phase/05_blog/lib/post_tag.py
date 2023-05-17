from dataclasses import dataclass

@dataclass
class PostTag:
    id: int
    post_id: int
    tag_id: int
