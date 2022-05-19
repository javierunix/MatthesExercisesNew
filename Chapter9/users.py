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

        return description.title()

    def greenting_user(self):
        print(f"\nWelcome {self.f_name.title()} {self.l_name.title()}. "
              f"We are very happy having you with us!!")

    def increment_logging_attempts(self, logging_attempts):
        """Increment the number of logging attempts."""
        self.logging_attempts += logging_attempts

    def reset_logging_attempts(self):
        """Reset number of loggings."""
        self.logging_attempts = 0


user = User('manolito', 'perez', 34, 'calle lobato', 'fontanero')

print(user.describe_user())

# Increment loggings number.
user.increment_logging_attempts(10)
print(user.describe_user())
user.increment_logging_attempts(10)
print(user.describe_user())


# Reset loggings number.
user.reset_logging_attempts()
print(user.describe_user())

