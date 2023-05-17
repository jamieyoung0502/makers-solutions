from dataclasses import dataclass

@dataclass
class Recipe:
    id: int
    title: str
    cooking_time: int
    rating: int