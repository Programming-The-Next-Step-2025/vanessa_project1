from collections import defaultdict
from .ingredients import IngredientList

class Pantry:
    """
    Represents a pantry that stores ingredient quantities and recipes.

    Attributes:
        pantry (defaultdict): Maps ingredient names to their quantities.
        recipes (defaultdict): Maps recipe names to IngredientList objects.
    """

    def __init__(self):
        """
        Initializes a Pantry object with empty pantry and recipe collections.
        """
        self.pantry = defaultdict(int)
        self.recipes = defaultdict(IngredientList)  # maps name -> IngredientList

    def add_to_pantry(self, item: str, quantity: int) -> dict:
        """
        Adds a specified quantity of an item to the pantry.

        Args:
            item (str): The name of the ingredient to add.
            quantity (int): The amount of the ingredient to add.

        Returns:
            dict: The updated pantry as a regular dictionary.
        """
        self.pantry[item] += quantity
        return dict(self.pantry)

    def add_to_recipes(self, name: str, ingredients: IngredientList):
        """
        Adds a recipe to the pantry's recipe collection.

        Args:
            name (str): The name of the recipe.
            ingredients (IngredientList): The list of ingredients for the recipe.
        """
        self.recipes[name] = ingredients

    def possible_recipe(self, recipe_name: str) -> bool:
        """
        Checks if a recipe can be made with the current pantry contents.

        Args:
            recipe_name (str): The name of the recipe to check.

        Returns:
            bool: True if the recipe can be made, False otherwise.
        """
        if recipe_name not in self.recipes:
            return False
        return self.recipes[recipe_name].enough_for_recipe(self)

    def lowest_calories_recipe(self):
        """
        Finds the recipe with the lowest calories that can be made from the pantry.

        Returns:
            str or None: The name of the recipe with the lowest calories, or None if no recipe can be made.
        """
        possible = [
            (name, recipe.total_calories)
            for name, recipe in self.recipes.items()
            if recipe.enough_for_recipe(self)
        ]
        if not possible:
            return None
        return min(possible, key=lambda x: x[1])[0]