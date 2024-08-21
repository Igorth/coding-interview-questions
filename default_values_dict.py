comboy = {
    'age': 33,
    'horse': 'mustang',
    'weight': 1500
}

# Use the get() method to retrieve a value
horse_name = comboy.get('horse')
print(horse_name)

# Use the get() method with a default value
horse_age = comboy.get('age', 0)
print(horse_age)

# Set default values
name = comboy.setdefault('name', 'my horse')
print(comboy.get('name'))
