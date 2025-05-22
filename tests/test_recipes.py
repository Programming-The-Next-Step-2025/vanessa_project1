import unittest
from recipe_book_project_vanessalulo.ingredients import Ingredient, IngredientList
from recipe_book_project_vanessalulo.recipes import Pantry

class TestPantrySystem(unittest.TestCase):

    def setUp(self):
        self.pantry = Pantry()

        # Ingredients
        self.chicken = Ingredient(name="chicken", measurement="g", quantity=200, calories=300)
        self.rice = Ingredient(name="rice", measurement="g", quantity=100, calories=130)
        self.broccoli = Ingredient(name="broccoli", measurement="g", quantity=50, calories=40)

        # IngredientList for recipe1
        self.recipe1 = IngredientList()
        self.recipe1.add_ingredient(self.chicken)
        self.recipe1.add_ingredient(self.rice)

        # IngredientList for recipe2
        self.recipe2 = IngredientList()
        self.recipe2.add_ingredient(self.broccoli)

        self.pantry.add_to_pantry("chicken", 200)
        self.pantry.add_to_pantry("rice", 100)
        self.pantry.add_to_pantry("broccoli", 20)  # Not enough yet

    def test_add_to_pantry(self):
        self.pantry.add_to_pantry("broccoli", 30)
        self.assertEqual(self.pantry.pantry["broccoli"], 50)

    def test_add_to_recipes(self):
        self.pantry.add_to_recipes("protein_rice", self.recipe1)
        self.assertIn("protein_rice", self.pantry.recipes)

    def test_possible_recipe_true(self):
        self.pantry.add_to_recipes("protein_rice", self.recipe1)
        self.assertTrue(self.pantry.possible_recipe("protein_rice"))

    def test_possible_recipe_false(self):
        self.pantry.add_to_recipes("veg_recipe", self.recipe2)
        self.assertFalse(self.pantry.possible_recipe("veg_recipe"))

    def test_lowest_calories_recipe(self):
        self.pantry.add_to_recipes("protein_rice", self.recipe1)  # 430 cal
        self.pantry.add_to_recipes("veg_recipe", self.recipe2)    # 40 cal (not enough broccoli yet)

        self.pantry.add_to_pantry("broccoli", 50)  # Now we can make it

        result = self.pantry.lowest_calories_recipe()
        self.assertEqual(result, "veg_recipe")

    def test_remove_ingredient(self):
        removed = self.recipe1.remove_ingredient("chicken")
        self.assertTrue(removed)
        self.assertNotIn("chicken", self.recipe1.ingredients)

    def test_remove_nonexistent_ingredient(self):
        removed = self.recipe1.remove_ingredient("tofu")
        self.assertFalse(removed)

    def test_enough_for_recipe(self):
        self.assertTrue(self.recipe1.enough_for_recipe(self.pantry))

    def test_not_enough_for_recipe(self):
        self.assertFalse(self.recipe2.enough_for_recipe(self.pantry))  # only 20g in pantry, 50g needed

if __name__ == '__main__':
    unittest.main()
