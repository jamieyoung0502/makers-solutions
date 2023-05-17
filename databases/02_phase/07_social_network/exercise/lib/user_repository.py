from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from users')
        return [User(row["id"], row["username"], row["email_address"]) for row in rows]

    def find(self, user_id):
        query = """
        SELECT *
        FROM users
        WHERE id = %s
        """
        user = self._connection.execute(query, [user_id])[0]
        return User(user["id"], user["username"], user["email_address"])

    def create(self, user):
        query = """
        INSERT INTO users
        (username, email_address)
        VALUES (%s, %s)
        """
        user = self._connection.execute(query, [user.username, user.email_address])

    def update(self, col_name, new_value, user_id):
        query = """
        UPDATE users
        SET {} = %s
        WHERE id = %s;
        """.format(col_name)

        self._connection.execute(query, [new_value, user_id])

    def delete(self, user_id):
        query = """
        DELETE FROM users
        WHERE id = %s;
        """
        self._connection.execute(query, [user_id])