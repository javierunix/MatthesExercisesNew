import unittest
from city_country import city_contry


class CityTestCase(unittest.TestCase):
    """Class to test the function city_country."""

    def test_city_country(self):
        """Test if cities like 'Santiago, Chile' work."""
        formatted_city = city_contry('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        """Test if cities like Santiago, Chile - Population: 5000000 work."""
        formatted_city = city_contry('santiago', 'chile', 5000000)
        self.assertEqual(
            formatted_city, 'Santiago, Chile - Population: 5000000')


if __name__ == '__main__':
    unittest.main()
