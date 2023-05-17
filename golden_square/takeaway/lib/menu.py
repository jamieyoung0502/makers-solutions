class Menu():

    def __init__(self, *args) -> None:
        self.dishes = []
        for dish in args:
            self.dishes.append(dish)

    def list_dishes(self):
        return [f"{dish.title.capitalize()} for £{dish.price}" for dish in self.dishes]