import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test for the class Employee."""

    def setUp(self):
        """
        Create a employee and set of rises.
        """
        first_name = 'Bryan'
        last_name = 'Smith'
        annual_salary = 120_000
        self.employee = Employee(first_name, last_name, annual_salary)
        self.rises = [None, 3000, 10000]

    def test_three_rises(self):
        salary = 120_000
        """Testa that the three rises are stored properly."""
        for rise in self.rises:
            if not rise:
                salary += 5000
            else:
                salary += rise
            self.assertEqual(self.employee.give_raise(rise), salary)


if __name__ == '__main__':
    unittest.main()
