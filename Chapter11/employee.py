class Employee:
    """Class to model a employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Define the employees attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, rise=None):
        """Increase the annual salary (5000$ default)."""
        if not rise:
            self.annual_salary += 5_000
            return self.annual_salary
        else:
            self.annual_salary += rise
            return self.annual_salary
