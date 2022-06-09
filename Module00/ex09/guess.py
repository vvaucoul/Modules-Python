from random import random
import sys

try:
    assert len(sys.argv) == 1, "Do not enter arguments !"
except AssertionError as e:
    print("AssertionError: " + e.__str__())
    sys.exit(1)

print("This is an interactive guessing game!\nYou have to enter a number \
between 1 and 99 to find out the secret number.\nType 'exit' to end \
the game. Good luck!")
print("\n")

number = int(random() * 99)
attempt = 0

while (1):
    sys.stdout.flush()
    print("What's your guess between 1 and 99?")

    while (True):
        try:
            guess = str(input(">> "))
        except EOFError:
            print("\nUse exit to quit the game instead of Ctrl+D!")
            continue
        if guess == "exit":
            print("Goodbye!")
            sys.exit(0)
        elif guess.isdigit():
            guess = int(guess)
            break
        else:
            print("Please enter a number between 1 and 99!")
            continue
    attempt += 1
    if (guess < number):
        print("Too low!")
    elif (guess > number):
        print("Too high!")
    else:
        if (number == 42):
            print(
                "The answer to the ultimate question of life,\
                    the universe and everything is 42.")
        if (attempt == 1):
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print("You won in " + str(attempt) + " attempts!")
        break
