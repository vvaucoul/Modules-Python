from datetime import datetime
from recipe import Recipe

class Book:
    name: str
    last_updated: datetime
    creation_date: datetime
    recipe_list: dict

    def __init__(self, name) -> None:
        if not name:
            raise ValueError("Name must not be empty")
        else:
            self.name = name
        self.last_updated = datetime.now()
        self.creation_date = datetime.now()
        self.recipe_list = {"starter": [], "lunch": [], "dessert": []}
        pass

    def get_recipe_by_name(self, name) -> Recipe:
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for recipe_type in self.recipe_list:
            for recipe in self.recipe_list[recipe_type]:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print("Recipe not found")
        pass

    def get_recipes_by_types(self, recipe_type) -> list:
        """Get all recipe names for a given recipe_type """
        if recipe_type not in self.recipe_list:
            raise ValueError("Recipe type must be a valid recipe type")
        elif not self.recipe_list[recipe_type]:
            raise ValueError("Recipe type not found")
        else:
            return self.recipe_list[recipe_type]
        pass

    def add_recipe(self, recipe) -> None:
        """Add a recipe to the book and update last_update"""
        if type(recipe) != Recipe:
            raise ValueError("Recipe type must be a Recipe type")
        elif recipe.recipe_type not in self.recipe_list:
            raise ValueError("Recipe type must be a valid recipe type")
        else:
            self.recipe_list[recipe.recipe_type].append(recipe)
            self.last_updated = datetime.now()
        pass
