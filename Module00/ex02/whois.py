import sys

try:
    assert not len(sys.argv) > 2, "more than one argument is provided"
    assert not len(sys.argv) <= 1, "no argument is provided"
    assert sys.argv[1].isnumeric(), "argument is not a number"
except AssertionError as e:
    print("AssertionError: " + e.__str__())
    sys.exit(1)

nbr = int(sys.argv[1])

if (int(nbr) == 0):
    print("I'm Zero.")
elif (int(nbr) % 2 == 0):
    print("I'm Even.")
elif (int(nbr) % 2 == 1):
    print("I'm Odd.")
