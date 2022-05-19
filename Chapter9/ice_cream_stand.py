class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializze name and cuisine type and number of served."""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant attributes."""
        descriptive_text = f"{self.name}, {self.type}, {self.number_served}."
        return f"Restaurant description: {descriptive_text.title()}"

    def open_restaurant(self):
        """Print a message telling that open."""
        print(f"The restaurant {self.restaurant_name.title()} is open.")

    def increment_number_served(self, number_served):
        """Increment number of serves"""
        self.number_served += number_served


class IceCreamStand(Restaurant):
    """A simple model for an Ice Cream Stand.
       This class is a child of the Restaurant Class.
    """

    def __init__(self, restaurant_name, cuisine_type='Ice Cream Stand'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'vanilla', 'chocolate']

    def describe_flavors(self):
        """Describe the list of flavors"""
        print(f"List of flavors: {self.flavors}")


valencianos = IceCreamStand('los valencianos')

print(valencianos.describe_restaurant())
valencianos.describe_flavors()
