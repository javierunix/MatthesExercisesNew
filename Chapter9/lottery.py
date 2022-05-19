from random import randint

primitive = list(range(1, 50))
print(primitive)

lottery_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                1, 2, 3, 4, 5, 6, 7, 8, 9]


def lottery_function(lottery_list):
    """Select randomly four elements from a list."""
    winner_ticket = []
    # Repeat the loop four times.
    for i in range(6):
        random_index = randint(0, len(lottery_list))
        chosen_element = lottery_list.pop(random_index - 1)
        winner_ticket.append(chosen_element)
    return winner_ticket


# Choose the winning number number.
winning_ticket = lottery_function(primitive[:])
# Order the elements to facilitate comparison.
winning_ticket.sort(key=lambda item:
                    ([str, int].index(type(item)), item))

# Choose the player number.


# Repeat the process until the player obtains the winning number.
#   Aditionally we define a counter.
total_counter = 0
# We are going to repeat the process 1000 times to estimate the probability.
num_of_cicles = 10
for i in range(num_of_cicles):
    counter = 1
    player_ticket = lottery_function(primitive[:])
    player_ticket.sort(key=lambda item:
                       ([str, int].index(type(item)), item))
    while player_ticket != winning_ticket:
        player_ticket = lottery_function(primitive[:])
        player_ticket.sort(key=lambda item:
                           ([str, int].index(type(item)), item))
        counter += 1
    total_counter += counter

print(f"The winning ticket is {winning_ticket}")
print(f"The player's ticket is {player_ticket}")
print(f"Estimated probability with {num_of_cicles} cicles:"
      f"{(num_of_cicles / total_counter) * 100} %")

