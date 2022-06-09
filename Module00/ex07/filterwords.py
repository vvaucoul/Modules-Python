import sys
import string

try:
    assert len(sys.argv) == 3, "Error: two arguments are expected"
    assert sys.argv[2].isdigit(), "Error: the second argument must be a number"
except AssertionError as error:
    print("AssertionError: " + error.__str__())
    sys.exit(1)

nbr = int(sys.argv[2])
str = sys.argv[1]

str = str.translate(str.maketrans('', '', string.punctuation))
arr = str.split()
narr = []
for item in arr:
    if (item.__len__() > nbr):
        narr.append(item)
print(narr)
