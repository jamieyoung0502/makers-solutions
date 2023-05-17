from dataclasses import dataclass
from datetime import date


@dataclass
class Order:
    id: int
    customer_id: int
    date: date
