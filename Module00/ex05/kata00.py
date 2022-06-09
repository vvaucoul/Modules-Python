t = (19, 42, 21)

if (len(t) != 3):
    print("Error: Entre a tupple with 3 elements")
    quit()
else:
    print("The 3 numbers are:", t.__str__().replace('(', '').replace(')', ''))
