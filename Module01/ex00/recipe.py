class Recipe:
    name: str
    cooking_lvl: int
    cooking_time: int
    ingredients: list
    description: str
    recipe_type: str

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type) -> None:
        if not name:
            raise ValueError("Name is empty")
        else:
            self.name = name
        if cooking_lvl < 1 or cooking_lvl > 5:
            raise ValueError("Cooking level must be between 1 and 5")
        else:
            self.cooking_lvl = cooking_lvl
        if cooking_time < 0:
            raise ValueError("Cooking time must be positive")
        else:
            self.cooking_time = cooking_time
        if not ingredients:
            raise ValueError("Ingredients are empty")
        else:
            self.ingredients = ingredients
        self.description = description
        if not recipe_type:
            raise ValueError("Recipe type is empty")
        self.recipe_type = recipe_type
        pass

    def __str__(self) -> str:
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "Name: " + self.name + "\n"
        txt += "Cooking level: " + str(self.cooking_lvl) + "\n"
        txt += "Cooking time: " + str(self.cooking_time) + "min\n"
        txt += "Ingredients: " + str(self.ingredients) + "\n"
        txt += "Description: " + self.description + "\n"
        txt += "Recipe type: " + self.recipe_type
        return txt