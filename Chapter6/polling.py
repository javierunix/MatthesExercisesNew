# Dictionary with the poll.
favorite_language = {
    'sonia': 'inglés',
    'nerea': 'castellano',
    'noa': 'ingles',
    'javier': 'latin'
}

# List of people.
people_list = ['sonia', 'alejandro', 'martín', 'nerea', 'roberto']

# Iterate over the list of people.
for person in people_list:
    # If the person took the pool.
    if person in favorite_language.keys():
        print(f"Thank you for responding, {person.title()}")
    # If the person didn't take the poll.
    else:
        print(f"{person.title()}, would you like to take our poll?")
