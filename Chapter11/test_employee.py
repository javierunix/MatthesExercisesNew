import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test for the class Employee."""

    def setUp(self):
        """
        Create a employee and set of rises.
        """
        self.quantity = 120_000  # Fix a quantity as salary to test rise.
        first_name = 'Bryan'
        last_name = 'Smith'
        self.employee = Employee(first_name, last_name, self.quantity)
        self.rises = [None, 3000, 10000]  # Test three different rises.

    def test_three_rises(self):
        """Test that the three rises are stored properly."""
        salary_test = self.quantity
        for rise in self.rises:
            if not rise:
                salary_test += 500
            else:
                salary_test += rise
            self.assertEqual(self.employee.give_raise(rise), salary_test)


if __name__ == '__main__':
    unittest.main()
