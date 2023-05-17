from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
When we call RecipeRepository#all
We get a list of Recipe objects reflecting the seed data.
"""
def test_all_records(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    recipes = repository.all()

    assert recipes == [
        Recipe(1, 'recipe1', 20, 5),
        Recipe(2, 'recipe2', 60, 3),
        Recipe(3, 'recipe3', 10, 5),
        Recipe(4, 'recipe4', 15, 5),
        Recipe(5, 'recipe5', 30, 4)
    ]

"""
When we call RecipeRepository#find
We get a single Recipe object reflecting the seed data.
"""

def test_find_specific_recipe(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    recipe = repository.find(1)
    assert recipe == Recipe(1, 'recipe1', 20, 5)