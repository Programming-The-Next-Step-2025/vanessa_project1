from collections import defaultdict

class Ingredient:
    def __init__(self, name: str, measurement: str, quantity: int, calories: int):
        self.name = name
        self.measurement = measurement
        self.quantity = quantity
        self.calories = calories

class IngredientList:
    def __init__(self):
        self.ingredients = defaultdict(lambda: None)
        self.total_calories = 0

    def add_ingredient(self, ingredient: Ingredient) -> bool:
        if self.ingredients[ingredient.name]:
            self.ingredients[ingredient.name].quantity += ingredient.quantity
            self.ingredients[ingredient.name].calories += ingredient.calories
        else:
            self.ingredients[ingredient.name] = ingredient
        self.total_calories += ingredient.calories
        return True

    def remove_ingredient(self, name: str) -> bool:
        if name in self.ingredients:
            self.total_calories -= self.ingredients[name].calories
            del self.ingredients[name]
            return True
        return False

    def contains_enough(self, name: str, quantity: int, pantry: 'Pantry') -> bool:
        return pantry.pantry.get(name, 0) >= quantity

    def enough_for_recipe(self, pantry: 'Pantry') -> bool:
        for ing in self.ingredients.values():
            if not self.contains_enough(ing.name, ing.quantity, pantry):
                return False
        return True
