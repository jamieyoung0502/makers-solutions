from dataclasses import dataclass


@dataclass
class Customer:
    id: int
    first_name: str
    last_name: str
