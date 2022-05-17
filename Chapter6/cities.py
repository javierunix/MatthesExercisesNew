# Dictionaty of dictionaries with data from three cities.
cities = {
    'madrid': {
        'country': 'spain',
        'population': 5e6,
        'interesting': 'museo del prado'
    },
    'london': {
        'country': 'united kingdom',
        'population': 13e6,
        'interesting': 'picadelly circus'
    },
    'paris': {
        'country': 'spain',
        'population': 10e6,
        'interesting': 'louvre museum'
    }
}

# Loop over the cities
for key, value in cities.items():
    print(f"City: {key.title()}")
    # Loop over the dict of each city
    for key, value in value.items():
        # If possible cast value to title format
        try:
            value = value.title()
        except AttributeError:
            value = value
        print(f"\t{key.title()}: {value}")
