from dataclasses import dataclass
from typing import List
from datetime import date

@dataclass
class Cohort:
    id: int
    name: str
    starting_date: date
    student_body: List[str] = None

# def __init__(self, id, name, genre, albums = None):
#     self.id = id
#     self.name = name
#     self.genre = genre
#     self.albums = albums or []