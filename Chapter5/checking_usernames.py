# List of current users.
current_users = ['sonia', 'andrés', 'manuel', 'nerea', 'noa']

# List of new users.
new_users = ['sonia', 'maría', 'julieta', 'pepe', 'miguel']

for user in new_users:
    if user in current_users:
        user = user.lower()
        print(f"{user} is not available, enter a new username.")
    else:
        print(f"{user} is available.")