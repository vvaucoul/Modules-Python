import sys

try:
    assert not len(
        sys.argv) == 1, "Usage: python operations.py <number1> <number2>\
\nExample:\n\
    python operations.py 10 3"
    assert not len(sys.argv) > 3, "InputError: too many arguments"
    assert not float(sys.argv[1]).is_integer() or \
        float(sys.argv[2]).is_integer(), "InputError: only numbers"
except AssertionError as e:
    print(e.__str__())
    exit()
except Exception as e:
    print("Error: only numbers are allowed")
    exit()

number1 = float(sys.argv[1])
number2 = float(sys.argv[2])

print("Sum:\t\t{}".format(int(number1 + number2)))
print("Difference:\t{}".format(int(number1 - number2)))
print("Product:\t{}".format(int(number1 * number2)))
if (number2 != 0):
    print("Quotient:\t{}".format(number1 / number2))
    print("Remainder:\t{}".format(int(number1 % number2)))
else:
    print("Quotient:\tERROR (div by zero)")
    print("Remainder:\tERROR (modulo by zero)")
