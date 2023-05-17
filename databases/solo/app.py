from lib.database_connection import DatabaseConnection
from lib.product_repository import ProductRepository
from lib.product import Product
from lib.order_repository import OrderRepository
from lib.customer_repository import CustomerRepository
import textwrap


class Application:
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/supermarket.sql")
        self._product_repository = ProductRepository(self._connection)
        self._order_repository = OrderRepository(self._connection)
        self._customer_repository = CustomerRepository(self._connection)

    def _product_info(self):
        name = input("Enter product name: ")
        quantity = int(input("Enter product price: "))
        price = float(input("Enter product price: "))

        return Product(None, name, quantity, price)

    def run(self):
        while True:
            print(
                textwrap.dedent(
                    """
                    What do you want to do?
                        1 = list all shop items
                        2 = create a new item
                        3 = list all orders
                        4 = create a new order
                        5 = exit
                    """
                )
            )

            try:
                selection = int(input())
            except ValueError:
                print("\nInvalid input. Please enter a number between 1 and 5")
                continue

            if selection == 1:
                product_all = self._product_repository.all()
                for product in product_all:
                    print(
                        f"#{product.id} {product.name} - unit price: {product.price} - quantity: {product.quantity}"
                    )

            elif selection == 2:
                new_product = self._product_info()
                if not self._product_repository.find(new_product.name):
                    self._product_repository.create(new_product)

                    product_all = self._product_repository.all()
                    for product in product_all:
                        print(
                            f"#{product.id} {product.name} - unit price: {product.price} - quantity: {product.quantity}"
                        )
                else:
                    print("\nThis product is already in the inventory!")

            elif selection == 3:
                order_all = self._order_repository.all()
                for order in order_all:
                    customer = self._customer_repository.find(order.customer_id)
                    print(
                        f"#{order.id} ordered on {order.date} by {customer.first_name} {customer.last_name}"
                    )

            elif selection == 4:
                customer_all = self._customer_repository.all()
                for customer in customer_all:
                    print(f"#{customer.id} {customer.first_name} {customer.last_name}")
                customer_id = input("\nEnter the id of the customer making an order: ")

                order_products = []

                while True:
                    inventory = self._product_repository.all()
                    options = [product.name for product in inventory]

                    for product in inventory:
                        print(
                            f"#{product.id} {product.name} - unit price: {product.price} - quantity: {product.quantity}"
                        )

                    selection = input(
                        "\nEnter the index of the item you would like to add. Press e to exit "
                    )

                    if selection == "e":
                        break

                    if selection in options:
                        quantity = int(input("\nHow many? "))
                        product = self._product_repository.find(selection)
                        if product.quantity >= quantity:
                            order_products.append((selection, quantity))
                        else:
                            print("sorry, we don't have that many in stock")
                        print(order_products)

                if order_products:
                    self._order_repository.create(customer_id, order_products)

                order_all = self._order_repository.all()
                for order in order_all:
                    customer = self._customer_repository.find(order.customer_id)
                    print(
                        f"#{order.id} ordered on {order.date} by {customer.first_name} {customer.last_name}"
                    )

            elif selection == 5:
                break
            else:
                print("Invalid selection. Please enter a number between 1 and 5")


if __name__ == "__main__":
    app = Application()
    app.run()

## removed for now:
## 1. see items associated with an order:
# try:
#     selection = str(
#         input(
#             "\nWould you like to see the items for a particular order? (y/n)"
#         )
#     )
# except ValueError:
#     print("\nInvalid input. Please enter y or n")
#     continue

# if selection == "y":
#     selection = str(
#         input(
#             "\nEnter the index of the order you'd like to see the items of"
#         )
#     )
# elif selection == "n":
#     break
