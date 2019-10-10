
import unittest
from unittest import TestCase
from unittest.mock import patch



import Bitcoins


class TestPriceOfBitcoins(TestCase):


 def test_get_price_of_bitcoins(self,mock_rates):
     mock_rates = 8,692.8000
     example_api_response = {'base': 'USD', 'date': '2019-02-04', 'rates': {'USD':mock_rates}}
     mock_rates.side_effect = [example_api_response]
     converted = Bitcoins.mock_rates(8692.8, 'USD')
     self.assertEqual(8692.8, converted)


if __name__ == '__main__':
    unittest.main()