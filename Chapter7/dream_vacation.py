# Program that pools users about their dream vacation.

# Empty dictionary to store poll results.
dream_vacation = {}

# Variable to control the loop status.
active = True

# Loop is active while 'active' is set to 'True'
while active:
    # Ask the user name.
    name = input("Whats your name?> ")
    name = name.lower()
    # Ask the user desired destination.
    response = input(f"If you could visit one place in the world"
                     f", where would you go?> ")
    response = response.lower()
    # Add the user and response to the dictionary.
    dream_vacation[name] = response
    new_user = input("Do you want to continue the poll? (yes/no)> ")
    # If not new_user, set active to 'False'.
    if new_user == 'no':
        active = False

print("\nPoll results:")
for key, value in dream_vacation.items():
    print(f"\t{key.title()} would like to visit {value.title()}.")
