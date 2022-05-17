# Create three dictionary with data from three people
person1 = {'first_name': 'noa', 'last_name': 'guijarro',
           'age': 3, 'city': 'san josé de la vega'}

person2 = {'first_name': 'nerea', 'last_name': 'guijarro',
           'age': 10, 'city': 'san josé de la vega'}

person3 = {'first_name': 'sonia', 'last_name': 'quesada',
           'age': 38, 'city': 'san josé de la vega'}

# Store all dicts in a list
people = [person1, person3, person3]

# Loop over the list and print all values.
for person in people:
    print(f"Values: {person.values()}")
