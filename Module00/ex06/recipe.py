import sys

cookbook = {
    "sandwich": (["ham", "bread", "cheese"], "lunch", "10"),
    "cake": (["flour", "sugar", "eggs"], "dessert", "60"),
    "salad": (["avocado", "arugula", "tomatoes", "spinach"], "lunch", "15"),
}


def __clear_screen__():
    print("\033c")


def print_cookbook():
    __clear_screen__()
    print("-" * 64)

    print("The CoookBook contain: " + str(len(cookbook.keys())) + " receipes")
    for recipe in cookbook.keys():
        print("- " + recipe)
    print("\nReceipes informations:")
    for recipe in cookbook.values():
        key = list(cookbook.keys())[list(cookbook.values()).index(recipe)]
        tmp_receipe = recipe[0].__str__().replace(
            "[",
            "").replace(
            "]",
            "").replace(
            "(",
            "").replace(
                ")",
                "").replace(
                    "'",
            "")
        time = recipe[1]
        preparation_time = recipe[2]
        print(key)
        print("- Ingredients: " + tmp_receipe)
        print("- Preparation: " + time)
        print("- Time: " + preparation_time + " minutes\n")
    print("-" * 64)


def print_receipe(receipename):
    if not cookbook.keys().__contains__(receipename):
        print("Invalid receipe name")
        return
    print("-" * 64)
    print("Receipe: " + receipename)
    print("Ingredients:")
    for ingredient in cookbook[receipename][0]:
        print("\t- " + ingredient)
    print("Preparation:")
    print("\t- " + cookbook[receipename][1])
    print("Time: " + cookbook[receipename][2] + " minutes")
    print("-" * 64)


def delete_receipe(receipe_index):
    key = list(cookbook.keys())[receipe_index]
    del cookbook[key]
    print("-" * 64)
    print("Receipe deleted !")
    print("-" * 64)


def add_receipe(receipename, ingredients, preparation, time):
    if cookbook.keys().__contains__(receipename):
        __clear_screen__()
        print("\033[1;31;1mError: Receipe already exist\033[0;37;0m")
        return
    cookbook[receipename] = (ingredients, preparation, time)
    print("-" * 64)
    print("Receipe added !")
    print("-" * 64)


def __main__():

    __clear_screen__()
    while (1):
        print("Please select an option by typing the corresponding number:")
        print("1: Add a receipe")
        print("2: Delete a receipe")
        print("3: Print a receipe")
        print("4: Print the CookBook")
        print("5: Quit")
        try:
            print(">> ", end=""),
            sys.stdout.flush()
            value = int(sys.stdin.readline())

        # No ascii option
        except ValueError:
            __clear_screen__()
            print("\033[1;31;1mError: Invalid option\033[0;37;0m")
            continue

        # Add a receipe
        if (value == 1):
            __clear_screen__()
            is_good = False
            while (not is_good):
                print("Enter receipe name:")
                print("> ", end=""),
                sys.stdout.flush()
                receipename = ""
                receipename = str(input())
                receipename.rstrip('\n')
                if (str(len(receipename)) == 0 or not receipename.isalpha()):
                    __clear_screen__()
                    print("\033[1;31;1mError: \
Invalid receipe name\033[0;37;0m")
                    continue
                else:
                    is_good = True

            is_good = False
            __clear_screen__()
            while (not is_good):
                print("Enter ingredients (use , to separate them):")
                print("> ", end=""),
                array_ingredients = []
                sys.stdout.flush()
                ingredients = ""
                ingredients = str(input())
                ingredients.rstrip('\n')
                for char in ingredients:
                    if char == ' ':
                        ingredients = ingredients.replace(char, "")
                if (str(len(ingredients)) == 0 or ingredients in "0123456789"):
                    __clear_screen__()
                    print("\033[1;31;1mError: Invalid ingredients\033[0;37;0m")
                    continue
                else:
                    array_ingredients = ingredients.split(",")
                    is_good = True

            is_good = False
            __clear_screen__()
            while (not is_good):
                print("Enter preparation:")
                print("> ", end=""),
                sys.stdout.flush()
                preparation = ""
                preparation = str(input())
                preparation.rstrip('\n')
                if (str(len(preparation)) == 0 or not preparation.isalpha()):
                    __clear_screen__()
                    print("\033[1;31;1mError: Invalid preparation\033[0;37;0m")
                    continue
                else:
                    is_good = True

            is_good = False
            __clear_screen__()
            while (not is_good):
                print("Enter time:")
                print("> ", end=""),
                sys.stdout.flush()
                time = ""
                time = str(input())
                time.rstrip('\n')
                if (str(len(time)) == 0 or not time.isdigit()
                        or int(time) <= 0):
                    __clear_screen__()
                    print("\033[1;31;1mError: Invalid time\033[0;37;0m")
                    continue
                else:
                    is_good = True

            add_receipe(receipename, array_ingredients, preparation, time)

        # Delete a receipe
        elif (value == 2):
            __clear_screen__()
            is_good = False
            if (len(cookbook.keys()) == 0):
                print("\033[1;31;1mError: CookBook is empty\033[0;37;0m")
                continue
            while (not is_good):
                print("Select a receipe:")
                for recipe in cookbook.keys():
                    index = list(cookbook.keys()).index(recipe) + 1
                    print("    - " + index.__str__() + ": " + recipe)
                print("> ", end=""),
                sys.stdout.flush()
                try:
                    receipe_index = int(sys.stdin.readline())
                    if (receipe_index > 0 and receipe_index <=
                            len(cookbook.keys())):
                        is_good = True
                    else:
                        __clear_screen__()
                        print("\033[1;31;1mError: Invalid option\033[0;37;0m")
                except ValueError:
                    __clear_screen__()
                    print("\033[1;31;1mError: Invalid option\033[0;37;0m")
            delete_receipe(receipe_index - 1)

        # Print a receipe
        elif (value == 3):
            __clear_screen__()
            is_good = False
            if (len(cookbook.keys()) == 0):
                print("\033[1;31;1mError: CookBook is empty\033[0;37;0m")
                continue
            while (not is_good):
                print("Select a receipe:")
                for recipe in cookbook.keys():
                    index = list(cookbook.keys()).index(recipe) + 1
                    print("    - " + index.__str__() + ": " + recipe)
                print("> ", end=""),
                sys.stdout.flush()
                receipename = sys.stdin.readline()
                try:
                    receipename = int(receipename)
                    if (receipename > 0 and receipename
                            <= len(cookbook.keys())):
                        is_good = True
                    else:
                        __clear_screen__()
                        print("\033[1;31;1mError: Invalid option\033[0;37;0m")
                except ValueError:
                    __clear_screen__()
                    print("\033[1;31;1mError: Invalid option\033[0;37;0m")
            __clear_screen__()
            print_receipe(list(cookbook.keys())[receipename - 1])
            continue

        # Print the cookbook
        elif (value == 4):
            print_cookbook()

        # Quit the cookbook
        elif (value == 5):
            __clear_screen__()
            print("Cookbook closed")
            break

        # Invalid Options < 1 || > 5
        else:
            __clear_screen__()
            print(
                "\033[1;31;1mError: This option does not exist, \
please type the corresponding number.\033[0;37;0m")
            continue


__main__()
