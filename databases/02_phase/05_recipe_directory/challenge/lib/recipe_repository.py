from lib.recipe import Recipe

class RecipeRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from recipes')
        return [Recipe(row["id"], row["title"], row["cooking_time"], row["rating"]) for row in rows]

    def find(self, recipe_id):
        query = """
        SELECT *
        FROM recipes
        WHERE id = %s
        """
        recipe = self._connection.execute(query, [recipe_id])[0]
        return Recipe(recipe["id"], recipe["title"], recipe["cooking_time"], recipe["rating"])