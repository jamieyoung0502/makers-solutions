class Dish:
    def __init__(self, title, price) -> None:

        if any(item == "" for item in [title, price]):
            raise Exception("enter a valid title and price")

        if not isinstance(price, (int, float)):
            raise Exception("enter a float for price")

        if not price > 0:
            raise Exception("enter a float greater than 0 for price")

        if not isinstance(title, str):
            raise Exception("enter a string for title")

        self.title = title
        self.price = float(price)