import sys

if (len(sys.argv) > 1):
    args = sys.argv[::-1]
    args.remove(sys.argv[0])
    res = ""
    index = 0

    for arg in args:
        str = arg[::-1]
        for char in str:
            if (char.isupper()):
                char = char.lower()
            else:
                char = char.upper()
            res += char
        if (arg != args[-1] and len(args[index + 1]) > 0):
            res += " "
        index += 1
    print(res)
