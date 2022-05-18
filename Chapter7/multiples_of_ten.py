number = int(input("Choose a number> "))

is_multiple = ''  # by default the answer is afirmative.

# if number is multiple of 10
if number % 10 != 0:
    is_multiple = 'not'  # we write not before the afirmation.

print(f"\nThe number {number} is {is_multiple} multiple of 10.")
