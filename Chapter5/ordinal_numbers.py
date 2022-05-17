# Loop to add the ordinal suffix to cardinal numbers.

# Define the suffix variable.
suffix = ''
for i in range(1, 10):
    if i == 1:
        suffix = 'st'
    elif i == 2:
        suffix = 'nd'
    elif i == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print(f"{i}{suffix}")