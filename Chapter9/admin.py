from users import User


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
