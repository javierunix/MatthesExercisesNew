players = ['charles', 'martina', 'michael', 'florence',
           'eli']  # create a list with five elements

# print first three items
print("The first three elements in the list are: ")
for item in players[:3]:
    print(item.title())

# print the three elements in the middle of the list
middle_term = len(
    players
) // 2  # the middle term is the integer part of dividing the length of the list by two
print("The three elements in the middle of the list are: ")
for item in players[middle_term - 1:middle_term + 2]:
    print(item.title())

# print the last three elements in the list
print("The last three elements in the list are: ")
for item in players[-3:]:
    print(item.title())

