from collections import defaultdict
from .ingredients import IngredientList
import plotly.graph_objects as go


class Pantry:
    """
    Represents a pantry that stores ingredient quantities and recipes.

    Attributes:
        pantry (defaultdict): Maps ingredient names to their quantities.
        recipes (defaultdict): Maps recipe names to IngredientList objects.
    """

    def __init__(self):
        """
        Initializes a Pantry  with empty pantry and recipe collections.
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

    def find_recipes_under(self, calories=400):
        """
        Finds all recipes that can be made with the current pantry contents and are under a specified calorie limit.

        Args:
            calories (int): The maximum calorie limit for the recipes.

        Returns:
            list: A list of recipe names that can be made and are under the calorie limit.
        """
        possible = [
            name
            for name, recipe in self.recipes.items()
            if recipe.enough_for_recipe(self) and recipe.total_calories < calories
        ]
        return possible
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
    
    def visualize_pantry(self):
            """
            Creates an interactive bar chart of the pantry contents using Plotly.
            """
            if not self.pantry:
                print("Pantry is empty.")
                return

            items = list(self.pantry.keys())
            quantities = list(self.pantry.values())

            fig = go.Figure(data=[
                go.Bar(name='Quantity', x=items, y=quantities)
            ])

            fig.update_layout(
                title="Pantry Ingredient Quantities",
                xaxis_title="Ingredient",
                yaxis_title="Quantity",
                template="plotly_white"
            )

            fig.show()