from dataclasses import dataclass

@dataclass
class Ship:
    length: int

# When the @dataclass decorator is used, it automatically generates several special methods
# for the class, including __init__, __repr__, and __eq__.
# These methods are used to create instances of the class, display information
# about instances of the class, and compare instances of the class for equality, respectively.


# @dataclass
# class Ship:
#     length: int
#     segments: List[ShipSegment] = None

#     def __post_init__(self):
#         if self.segments is None:
#             self.segments = [ShipSegment(row=0, col=col) for col in range(self.length)]

#     def place(self, row: int, col: int, orientation: str):
#         # code to place the ship on the board...

#     def move(self, dx: int, dy: int):
#         for segment in self.segments:
#             segment.row += dy
#             segment.col += dx


# from dataclasses import dataclass

# @dataclass
# class Person:
#     name: str
#     age: int

# def __init__(self, name: str, age: int):
#     self.name = name
#     self.age = age

# def __repr__(self):
#     return f"Person(name={self.name}, age={self.age})"

# def __eq__(self, other):
#     if isinstance(other, Person):
#         return self.name == other.name and self.age == other.age
#     return False