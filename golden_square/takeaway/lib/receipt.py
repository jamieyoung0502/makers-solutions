from lib.order import Order

class Receipt:
    def __init__(self, order) -> None:
        if not isinstance(order, Order):
            raise ValueError("Only an instance of the Order class can be added")

        if not order.dishes:
            raise Exception("empty orders are not valid")

        self.order = order

    def grand_total(self):
        total = sum((dish["price"] * dish["quantity"]) for dish in self.order.dishes.values())
        return "{:.2f}".format(total)