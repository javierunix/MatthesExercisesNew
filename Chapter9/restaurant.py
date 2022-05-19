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

