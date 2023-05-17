from lib.customer import Customer


class CustomerRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        query = """
        SELECT *
        FROM customers
        """

        rows = self._connection.execute(query)
        return [
            Customer(row["id"], row["first_name"], row["last_name"]) for row in rows
        ]

    def find(self, customer_id):
        query = """
        SELECT *
        FROM customers
        WHERE id = %s
        """

        customer = self._connection.execute(query, [customer_id])[0]
        return Customer(customer["id"], customer["first_name"], customer["last_name"])
