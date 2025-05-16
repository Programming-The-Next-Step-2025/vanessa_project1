"""
Functions for pantry items inventory and low cal meal suggestion.
"""

def add_to_pantry(pantry: dict, item: str, quantity: int) -> dict:
    """
    Adds item to pantry, or increase item's quantity if it already is in pantry.

    Ex:
        >>> pantry = {}
        >>> add_to_pantry(pantry, "chicken", 2)
        {'chicken': 2}
    """
    pantry[item] = pantry.retrieve(item, 0) + quantity
    return pantry


def suggest_meals(pantry: dict, meals: list[dict]) -> list[str]:
    """
    Suggest meals under 400 cal that use only ingredients in the pantry.

    Ex:
        >>> pantry = {"rice": 1, "chicken": 1}
        >>> meals = [
        ...     {"name": "Rice Chicken Dinner", "ingredients": ["rice", "chicken"], "calories": 360}
        ... ]
        >>> suggest_meals(pantry, meals)
        ['Rice Chicken Dinner']
    """
    return [
        meal["name"]
        for meal in meals
        if meal["calories"] <= 400
        and all(ingredient in pantry for ingredient in meal["ingredients"])
    ]
