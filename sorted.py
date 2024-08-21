animals = [
    {'type': 'penguins', 'name': 'jogn', 'age': 9},
    {'type': 'elephants', 'name': 'elephant1', 'age': 12},
    {'type': 'zebras', 'name': 'zebra1', 'age': 7},
    {'type': 'lions', 'name': 'leo', 'age': 14},
    {'type': 'giraffes', 'name': 'giraffe1', 'age': 10},
]

sorted_dict = sorted(animals, key=lambda animal: animal['type'])
print(sorted_dict)


print(sorted([6, 4, 2, 3, 1, 0]))
print(sorted(['dog', 'cat', 'bird', 'elephant', 'mouse', 'fish'], reverse=True))