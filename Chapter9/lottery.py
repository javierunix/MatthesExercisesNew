from random import randint

lottery_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                1, 2, 3, 4, 5, 6, 7, 8, 9]


def lottery_function(lottery_list):
    """Select randomly four elements from a list."""
    winner_ticket = []
    # Repeat the loop four times.
    for i in range(4):
        random_index = randint(1, len(lottery_list))
        chosen_element = lottery_list.pop(random_index - 1)
        winner_ticket.append(chosen_element)
    return winner_ticket


# Choose the winning number number.
winning_ticket = lottery_function(lottery_list[:])
# Order the elements to facilitate comparison.
winning_ticket.sort(key=lambda item:
                    ([str, int].index(type(item)), item))

# Choose the player number.
player_ticket = lottery_function(lottery_list[:])
player_ticket.sort(key=lambda item:
                   ([str, int].index(type(item)), item))


# Repeat the process until the player obtains the winning number.
#   Aditionally we define a counter.
counter = 1
while player_ticket != winning_ticket:
    player_ticket = lottery_function(lottery_list[:])
    player_ticket.sort(key=lambda item:
                       ([str, int].index(type(item)), item))
    counter += 1

print(f"The winning ticket is {winning_ticket}")
print(f"The player's ticket is {player_ticket}")
print(f"Number of attempts: {counter}")
