from lib.order import Order
from lib.product_repository import ProductRepository
import datetime


class OrderRepository:
    def __init__(self, connection) -> None:
        self._connection = connection
        self._product_repository = ProductRepository(connection)

    def all(self):
        query = """
        SELECT *
        FROM orders
        """
        rows = self._connection.execute(query)
        return [Order(row["id"], row["customer_id"], row["date"]) for row in rows]

    def create(self, customer_id, order_products):
        query = """
        INSERT INTO orders
        (customer_id, date)
        VALUES(%s, %s)
        RETURNING id;
        """

        new_order = self._connection.execute(
            query, [customer_id, datetime.datetime.now().date().strftime("%Y-%m-%d")]
        )

        last_order_id = new_order[0]["id"]

        for order_product in order_products:
            query = """
            INSERT INTO order_products
            (order_id, product_id, quantity)
            VALUES(%s, %s, %s);
            """
            product = self._product_repository.find(order_product[0])

            self._connection.execute(
                query,
                [last_order_id, product.id, order_product[1]],
            )

        return None
