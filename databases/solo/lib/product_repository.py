from lib.product import Product


class ProductRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        query = """
        SELECT *
        FROM products
        """
        rows = self._connection.execute(query)
        return [
            Product(row["id"], row["name"], row["quantity"], float(row["price"]))
            for row in rows
        ]

    def find(self, product_name):
        query = """
        SELECT *
        FROM products
        WHERE name = %s
        """

        try:
            product = self._connection.execute(query, [product_name])[0]
            return Product(
                product["id"], product["name"], product["quantity"], product["price"]
            )
        # IndexError: for when you try to access a sequence (such as a list, tuple, or string) using an index that is out of range
        except IndexError:
            return None

    def create(self, new_product):
        query = """
        INSERT INTO products
        (name, quantity, price)
        VALUES(%s, %s, %s)
        """

        self._connection.execute(
            query, [new_product.name, new_product.quantity, new_product.price]
        )
        return None
