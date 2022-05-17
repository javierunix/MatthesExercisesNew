# Make a list of 5 or more usernames
usernames = ['admin', 'paloma', 'javier', 'jose', 'teresa']

# Check if there are users in the lists.
if len(usernames) == 0:
    print("We need to find more users.")

else:
    for username in usernames:
        username = username.title()
        # Print a specific message for admin.
        if username == 'Admin':
            print(f"Hello {username.lower()}, would do you like to see a status"
              f" report?")
        # Print a generic message for rest of users.
        else:
            print(f"Hello {username}, thank you for logging it again.")