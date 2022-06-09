import datetime

t = (3, 30, 2019, 9, 25)

if len(t) != 5:
    print("Error: The tuple has not 5 items")
    print("       Use format: (hour, minute, year, month, day")
    quit()

time = ""
tmp = ""

if (t[3] < 1):
    tmp = "1"
elif (t[3] < 10):
    tmp = "0" + str(t[3])
elif (t[3] > 12):
    tmp = "1"
else:
    tmp = str(t[3])
time += tmp + "/"

if (t[4] < 1):
    tmp = "1"
elif (t[4] < 10):
    tmp = "0" + str(t[4])
elif (t[4] > 31):
    tmp = "1"
else:
    tmp = str(t[4])
time += tmp + "/"
time += str(t[2]) + " "

if (t[0] < 0):
    tmp = "0"
elif (t[0] < 10):
    tmp = "0" + str(t[0])
elif (t[0] > 24):
    tmp = "1"
else:
    tmp = str(t[0])
time += tmp + ":"

if (t[1] < 0):
    tmp = "0"
elif (t[1] < 10):
    tmp = "0" + str(t[1])
elif (t[1] > 59):
    tmp = "0"
else:
    tmp = str(t[1])
time += tmp
print(time)
