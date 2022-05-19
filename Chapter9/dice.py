from random import randint


class Dice:
    """An simple attempt to model a dice."""

    def __init__(self, sides_number=6):
        """Set the dice's number of sides (default=6)."""
        self.sides_number = sides_number
        print(f"\nSetting a Dice object with {self.sides_number} sizes.")

    def roll_dice(self):
        """Give a random number between 1 and sides_number."""
        random_num = randint(1, self.sides_number)
        print(f'Random number: {random_num}.')


# Set the number of attempts.
number_of_attempts = 10

# Initialize a dice with the default number of sides.
dice1 = Dice()
for i in range(number_of_attempts):
    dice1.roll_dice()

# Initialize a dice with the 10 of sides.
dice2 = Dice(10)
for i in range(number_of_attempts):
    dice2.roll_dice()


