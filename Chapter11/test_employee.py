import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test for the class Employee."""

    def setUp(self):
        """
        Create a employee and set of rises.
        """
        question = int(input("Enter a salary to test give_rise()> "))
        self.quantity = question  # Fix a quantity as salary to test rise.
        first_name = 'Bryan'
        last_name = 'Smith'
        self.employee = Employee(first_name, last_name, self.quantity)
        self.rises = []

        while True:
            rise = input("Enter rise ('q' to quit)> ")
            if rise == 'q':
                break
            else:
                if rise == '':
                    rise = None
            try:
                self.rises.append(int(rise))
            except TypeError:
                self.rises.append(rise)

    def test_three_rises(self):
        """Test that the three rises are stored properly."""
        salary_test = self.quantity
        for rise in self.rises:
            if not rise:
                salary_test += 4000
            else:
                salary_test += rise
            self.assertEqual(self.employee.give_raise(rise), salary_test)


if __name__ == '__main__':
    unittest.main()
