from recipe_book_project_vanessalulo import add_to_pantry, suggest_meals

def test_add_to_pantry():
    pantry = {}
    result = add_to_pantry(pantry, "chicken", 2)
    assert result == {"chicken": 2}

def test_suggest_meals():
    pantry = {"rice": 1, "chicken": 1}
    meals = [{"name": "Chicken and Rice Dinner", "ingredients": ["rice", "chicken"], "calories": 360}]
    result = suggest_meals(pantry, meals)
    assert result == ["Chicken and Rice Dinner"]
