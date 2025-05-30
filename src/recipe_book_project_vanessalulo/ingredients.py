from collections import defaultdict

class Ingredient:
    """
    Represents a single ingredient with its properties.

    Attributes:
        name (str): The name of the ingredient.
        measurement (str): The unit of measurement for the ingredient.
        quantity (int): The quantity of the ingredient.
        calories (int): The calorie count for the ingredient.
    """
    def __init__(self, name: str, measurement: str, quantity: int, calories: int):
        """
        Initializes an Ingredient object.

        Args:
            name (str): The name of the ingredient.
            measurement (str): The unit of measurement.
            quantity (int): The quantity of the ingredient.
            calories (int): The calorie count.
        """
        self.name = name
        self.measurement = measurement
        self.quantity = quantity
        self.calories = calories

class IngredientList:
    """
    Represents a collection of Ingredient objects for a recipe.

    Attributes:
        ingredients (defaultdict): Maps ingredient names to Ingredient objects.
        total_calories (int): The total calories of all ingredients in the list.
    """
    def __init__(self):
        """
        Initializes an IngredientList with an empty ingredient collection and zero calories.
        """
        self.ingredients = defaultdict(lambda: None)
        self.total_calories = 0

    def add_ingredient(self, ingredient: Ingredient) -> bool:
        """
        Adds an ingredient to the list, updating quantity and calories if it already exists.

        Args:
            ingredient (Ingredient): The ingredient to add.

        Returns:
            bool: True if the ingredient was added or updated.
        """
        if self.ingredients[ingredient.name]:
            self.ingredients[ingredient.name].quantity += ingredient.quantity
            self.ingredients[ingredient.name].calories += ingredient.calories
        else:
            self.ingredients[ingredient.name] = ingredient
        self.total_calories += ingredient.calories
        return True

    def remove_ingredient(self, name: str) -> bool:
        """
        Removes an ingredient from the list by name.

        Args:
            name (str): The name of the ingredient to remove.

        Returns:
            bool: True if the ingredient was removed, False if not found.
        """
        if name in self.ingredients:
            self.total_calories -= self.ingredients[name].calories
            del self.ingredients[name]
            return True
        return False

    def contains_enough(self, name: str, quantity: int, pantry: 'Pantry') -> bool:
        """
        Checks if the pantry contains enough of a specific ingredient.

        Args:
            name (str): The name of the ingredient.
            quantity (int): The required quantity.
            pantry (Pantry): The pantry to check against.

        Returns:
            bool: True if the pantry has enough, False otherwise.
        """
        return pantry.pantry.get(name, 0) >= quantity

    def enough_for_recipe(self, pantry: 'Pantry') -> bool:
        """
        Checks if all ingredients in the list are available in sufficient quantity in the pantry.

        Args:
            pantry (Pantry): The pantry to check against.

        Returns:
            bool: True if all ingredients are available in required quantities, False otherwise.
        """
        for ing in self.ingredients.values():
            if not self.contains_enough(ing.name, ing.quantity, pantry):
                return False
        return True