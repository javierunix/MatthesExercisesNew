import json


def favorite_number(filename):
    """
    Function that ask the favorite number and save it in txt file.
    If the txt file already present, prints the favorite number.
    """
    try:
        with open(filename, 'r') as f:
            number = json.load(f)
            print(f"I know your favorite number! It is {number}.")
    except FileNotFoundError:
        number = int(input('Enter your favorite number> '))
        with open(filename, 'w') as f:
            json.dump(number, f)
            print('I will remember the number ;-)')


favorite_number('favorite_number_remember.json')
