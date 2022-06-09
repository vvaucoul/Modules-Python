languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

for item in languages:
    if not item:
        print("Error: An item is empty")
        quit()
    elif not languages[item]:
        print("Error: A value of an item is empty")
        quit()

if len(languages) != 3:
    print("Error: The dictionary has not 3 items")
    quit()

for item in languages:
    print("{} was created by {}".format(item, languages[item]))
