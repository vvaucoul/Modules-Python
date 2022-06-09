from operator import le

t = (0, 4, 132.42222, 10000, 12345.67)

if len(t) != 5:
    print("Error: The tuple has not 5 items")
    quit()

module = ""
ex = ""
f = t[2]
exp = t[3]
exp2 = t[4]

if (len(str(t[0])) == 1):
    module = "0" + str(t[0])
else:
    module = str(t[0])

if (len(str(t[1])) == 1):
    ex = "0" + str(t[1])
else:
    ex = str(t[1])

print(
    "module_" +
    module +
    ", " +
    "ex_" +
    ex +
    " : " +
    "{:.2f}, {:.2e}, {:.2e}".format(
        f,
        exp,
        exp2))
