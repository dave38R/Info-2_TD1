import json

animals = open('animal.json', "r")
equipment = open('equipment.json', 'r')

# Reading from file
animals = json.loads(animals.read())
equipment = json.loads(equipment.read())

# Printing keys and values from the dictionnary
for animal in animals.keys():
    print('animal ', animal, animals[animal])

for tool in equipment:
    print('equipement ', tool, equipment[tool])

for animal in animals:
    print(animal, type(animal))