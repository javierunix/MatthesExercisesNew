# Make a list with names of sandwiches
sandwich_ordes = ['pastrami', 'vegetal', 'pastrami', 'tunna',
                  'chicken', 'pork', 'beef', 'pastrami']

# Empty list for finished ordes.
finished_sandwiches = []

print('Sorry, in deli we run out of pastrami.')

# Remove all pastrami ocurrences.
while 'pastrami' in sandwich_ordes:
    sandwich_ordes.remove('pastrami')

# While sandwich orders are left loop through the list.
while sandwich_ordes:
    current_order = sandwich_ordes.pop()  # Pop last element.
    print(f"I made your {current_order} sandwich.")  # Print a message.
    finished_sandwiches.append(current_order)  # Append to the new list.

# Listing the made sandwiches.
print("\nThese are the sandwiches that have been made:")
for finished_sandwich in finished_sandwiches:
    print(f"\t{finished_sandwich.title()}.")
