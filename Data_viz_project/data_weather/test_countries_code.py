import unittest
from country_codes import get_country_code

class CountryCodesTestCase(unittest.TestCase):
    """Test_get_code"""
    def test_get_country_code(self):
        country_code = get_country_code('Andorra')
        self.assertEqual(country_code,'ad')

        country_code = get_country_code('Vietnam')
        self.assertEqual(country_code,'vn')

unittest.main()

