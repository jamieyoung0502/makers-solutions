from lib.dish import Dish

class Order:
    def __init__(self) -> None:
        self.dishes = {}

    def add_to_order(self, dish):
        if not isinstance(dish, Dish):
            raise ValueError("Only Dish instances can be added")

        if not self.dishes.get(dish.title):
            self.dishes[dish.title] = {"price" : dish.price, "quantity" : 1, "sum" : dish.price}
        else:
            self.dishes.get(dish.title)["quantity"] += 1
            self.dishes.get(dish.title)["sum"] += dish.price