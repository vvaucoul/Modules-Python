import time
import datetime
from time import sleep

def ft_progress(lst):
    start = datetime.datetime.now()
    do = False
    for i in range(len(lst)):
        if i == 0:
            i = 1
        elif i == len(lst) - 1:
            i = len(lst)
        remaining = (len(lst) - i) * (datetime.datetime.now() - start) / i
        elapsed = (datetime.datetime.now() - start)

        sec = float(remaining.total_seconds())
        sec_elapsed = float(elapsed.total_seconds())

        print("\r", end="")
        print("ETA: ", end='')
        percent = int(i / len(lst) * 100)

        print("{:.2f}s".format(sec), end=' ')
        print("[{:>3}%]".format(percent), end=' ')

        print("[{:<25}] {}/{} | elapsed time {:>.2f}s".format('=' *
              int(percent / 4) + ">", i, len(lst), sec_elapsed), end=' ')
        if i == len(lst) or i == 1:
            i = i - 1
            if not do:
                i = i + 1
                do = True
        if len(lst) == 1:
            yield lst[0]
        else:
            yield lst[i]


# Test MAIN

# listy = range(1000)
# ret = 0
# for elem in ft_progress(listy):
#     ret += (elem + 3) % 5
#     sleep(0.01)
# print()
# print(ret)
