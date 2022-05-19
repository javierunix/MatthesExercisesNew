class User:
    def __init__(self, first_name, last_name, age,
                 address, job):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        self.address = address
        self.job = job
        self.logging_attempts = 0

    def describe_user(self):
        print("\nUser data:")
        description = (f"Name: {self.f_name} {self.l_name}\n"
                       f"Age: {self.age}\n"
                       f"Adress: {self.address} {self.job}\n"
                       f"Loggings number: {self.logging_attempts}")

        print(f"{description.title()}")

    def greenting_user(self):
        print(f"\nWelcome {self.f_name.title()} {self.l_name.title()}. "
              f"We are very happy having you with us!!")

    def increment_logging_attempts(self, logging_attempts):
        """Increment the number of logging attempts."""
        self.logging_attempts += logging_attempts

    def reset_logging_attempts(self):
        """Reset number of loggings."""
        self.logging_attempts = 0


class Admin(User):
    """A model of an admin user"""

    def __init__(self, first_name, last_name, age, address, job):
        super().__init__(first_name, last_name, age, address, job)
        self.privileges = Privileges()

    def describe_privileges(self):
        print(f"\nAdmin privileges: {self.privileges}")


class Privileges:
    """A model of admin privileges"""

    def __init__(self):
        self.privileges = ["can add user", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"\nPrivileges: {self.privileges}")


# Create an admin instance.
admin = Admin('manolo', 'caracol', 55, 'lobato', 'driver')

admin.describe_user()
admin.privileges.show_privileges
