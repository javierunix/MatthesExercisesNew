import json

filename = 'favorite_number.txt'

try:
    with open(filename, 'r') as f:
        number = json.load(f)
        print(f"I know your favorite number! It is {number}.")
except FileNotFoundError:
    print(f"Sorry, I couldn't find the file '{filename}'.")
