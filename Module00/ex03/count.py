import sys
import string


def text_analyzer(*args):
    """this function counts the number of upper characters, lower characters, \
punctuation and spaces in a given text."""

    try:
        assert not len(args) > 1, "You must enter only one text to analyze"
    except AssertionError as e:
        print("AssertionError: " + e.__str__())
        return

    if (len(args) == 0):
        print("What is the text to analyze?")
        print(">> ", end="")
        text = input()
    else:
        text = args[0]

    upper = 0
    lower = 0
    punctuation = 0
    space = 0
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isspace():
            space += 1
        elif (char in string.punctuation):
            punctuation += 1
    print("The text contains {} characters".format(len(text)))
    print("- {} upper letters".format(upper))
    print("- {} lower letters".format(lower))
    print("- {} punctuation characters".format(punctuation))
    print("- {} spaces".format(space))
