import sys

phrase = "The right format"

length = len(phrase)
if (len(phrase) > 42):
    sys.stdout.write(phrase[0:42])
else:
    for i in range(42 - length):
        sys.stdout.write("-")
    sys.stdout.write(phrase)
