from dataclasses import dataclass

@dataclass
class Post:
    id: int
    title: str
    content: str
    views: int
    user_id: int