
from lib.recipe import Recipe

"""
Creates an instance of Recipe with an id, time and rating
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Recipe1", 25, 4)
    assert recipe.id == 1
    assert recipe.title == "Recipe1"
    assert recipe.cooking_time == 25
    assert recipe.rating == 4

"""
We can format recipes to look nice
"""
def test_recipes_format_nicely():
    recipe = Recipe(1, "Recipe1", 25, 4)
    assert str(recipe) == "Recipe(id=1, title='Recipe1', cooking_time=25, rating=4)"

"""
We can compare two identical recippes
And have them be equal
"""
def test_two_recipes_are_equal():
    recipe_1 = Recipe(1, "Recipe1", 25, 4)
    recipe_2 = Recipe(1, "Recipe1", 25, 4)
    assert recipe_1 == recipe_2

