class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializze name and cuisine type and number of served."""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant attributes."""
        descriptive_text = f"{self.name}, {self.type}, {self.number_served}"
        return descriptive_text.title()

    def open_restaurant(self):
        """Print a message telling that open."""
        print(f"The restaurant {self.restaurant_name.title()} is open.")

    def increment_number_served(self, number_served):
        """Increment number of serves"""
        self.number_served += number_served


# Initialize an object of the class.
restaurant = Restaurant('the great wall', 'chinese')

print(restaurant.describe_restaurant())
restaurant.increment_number_served(10)
print(restaurant.describe_restaurant())
restaurant.increment_number_served(10)
print(restaurant.describe_restaurant())
