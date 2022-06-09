from curses.ascii import isalnum
import sys

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

try:
    assert sys.argv.__len__() >= 2, "Please enter at least one string"
    for item in sys.argv:
        if item != sys.argv[0]:
            for char in item:
                if char == ' ':
                    continue
                else:
                    assert char.isalnum(), "Please enter only alphanumeric \
characters"
except AssertionError as e:
    print("AssertionError: " + e.__str__())
    sys.exit(1)

arr = []
for m in sys.argv:
    if m != sys.argv[0]:
        message = m.upper()
        message = ' '.join(message.split())
        arr.append(message)

for item in arr:
    for char in item:
        if char == ' ':
            print('/', end=' ')
        else:
            print(MORSE_CODE_DICT[char], end=' ')
    if (item != arr[-1]):
        print('/', end=' ')
print()
