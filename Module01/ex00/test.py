from book import Book
from recipe import Recipe

# Recipe Class

print("- Test recipe class")
input()

tourte = Recipe("Tourte", 5, 30, [
                "Tomate", "Fromage", "Oignon"], "Cuisson d'une tourte", "lunch")
to_print = str(tourte)
print(to_print)
input()
salad = Recipe("Salade", 2, 5, ["Tomate", "Salade", "Jambon",
                                "Oignon", "Huile"], "Préparation d'une salade", "starter")
to_print = str(salad)
print(to_print)
input()

# Check errors

try:
    burger = Recipe("Burger", -1, -1, ["Tomate", "Salade",
                    "Jambon"], "Préparation d'un burger", "lunch")
except ValueError as e:
    print(e)

try:
    burger = Recipe("", -1, -1, [], "", "")
except ValueError as e:
    print(e)

try:
    burger = Recipe("Burger", 5, -1, [], "", "")
except ValueError as e:
    print(e)

try:
    burger = Recipe("Burger", 5, 15, [], "", "")
except ValueError as e:
    print(e)

try:
    burger = Recipe("Burger", 5, 15, ["Salade", "Steak", "Tomate"], "", "")
except ValueError as e:
    print(e)

try:
    burger = Recipe("Burger", 5, 15, [
                    "Salade", "Steak", "Tomate"], "", "lunch")
    print("Valid Burger Recipe !")
except ValueError as e:
    print(e)

# Book Class
input()
print("- Test Book class")
input()

book = Book("Book")
print("  - Add recipe to book")
book.add_recipe(tourte)
burger = Recipe("Burger", 5, 15, [
    "Salade", "Steak", "Tomate"], "", "lunch")
book.add_recipe(burger)
input()
print("  - Get recipe Tourte and get instance")
tourte_insance = book.get_recipe_by_name("Tourte")
input()
print("  - Change tourte instance description")
tourte_insance.description = "Cuisson d'une tourte modifiée"
tourte_insance = book.get_recipe_by_name("Tourte")
input()
print("  - Get recipe by type 'lunch'")
dict_recipes = book.get_recipes_by_types("lunch")
input()
for recipe in dict_recipes:
    print(recipe)

print("- Book Errors")
input()
try:
    dict_recipes = book.get_recipes_by_types("testerror")
except ValueError as e:
    print(e)

try:
    dict_recipes = book.get_recipes_by_types("starter")
except ValueError as e:
    print(e)

try:
    dict_recipes = book.get_recipe_by_name("")
except ValueError as e:
    print(e)

try:
    dict_recipes = book.get_recipe_by_name("test")
except ValueError as e:
    print(e)

try:
    dict_recipes = book.add_recipe("test")
except ValueError as e:
    print(e)

try:
    dict_recipes = book.add_recipe(124)
except ValueError as e:
    print(e)

try:
    dict_recipes = book.add_recipe(444)
except ValueError as e:
    print(e)
