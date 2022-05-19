class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializze name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant attributes."""
        print(f"\n- Restaurant_name: {self.restaurant_name.title()}.")
        print(f"- Cuisine type: {self.cuisine_type}.")

    def open_restaurant(self):
        """Print a message telling that open."""
        print(f"The restaurant {self.restaurant_name.title()} is open.")


# Initialize an object of the class.
restaurant1 = Restaurant('the great wall', 'chinese')
restaurant2 = Restaurant('los pollos hermanos', 'mexican')
restaurant3 = Restaurant('oh la la', 'french')


# Calling the class methods.
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

