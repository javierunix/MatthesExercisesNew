import json

favorite_number = int(input('Enter your favorite number> '))


filename = 'favorite_number.txt'

with open(filename, 'w') as f:
    json.dump(favorite_number, f)
    print('I will remember the number ;-)')
