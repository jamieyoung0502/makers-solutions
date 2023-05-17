from dataclasses import dataclass
from typing import List

@dataclass
class Post:
    id: int
    title: str
    content: str
    comments: List[str] = None
