rivers = {
    'danubio': 'austria',
    'amazonas': 'brasil',
    'nilo': 'egipto',
    'ganges': 'india'
}

# Use a for loop to print a sentence about each river.
for key, value in rivers.items():
    print(f"El río {key.title()} pasa por {value.title()}.")

# Use a for loop to print the countries.
for value in rivers.values():
    print(value)

# Use a for loop to print the rivers' names.
for key in rivers.keys():
    print(key)
