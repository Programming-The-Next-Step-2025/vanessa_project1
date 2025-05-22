from collections import defaultdict
from .ingredients import IngredientList

class Pantry:
    def __init__(self):
        self.pantry = defaultdict(int)
        self.recipes = defaultdict(IngredientList)  # maps name -> IngredientList

    def add_to_pantry(self, item: str, quantity: int) -> dict:
        self.pantry[item] += quantity
        return dict(self.pantry)

    def add_to_recipes(self, name: str, ingredients: IngredientList):
        self.recipes[name] = ingredients

    def possible_recipe(self, recipe_name: str) -> bool:
        if recipe_name not in self.recipes:
            return False
        return self.recipes[recipe_name].enough_for_recipe(self)

    def lowest_calories_recipe(self):
        possible = [
            (name, recipe.total_calories)
            for name, recipe in self.recipes.items()
            if recipe.enough_for_recipe(self)
        ]
        if not possible:
            return None
        return min(possible, key=lambda x: x[1])[0]
