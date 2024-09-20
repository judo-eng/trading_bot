
# tests/test_data_fetcher.py
import unittest
from unittest.mock import patch
import data_fetcher

class TestDataFetcher(unittest.TestCase):

    @patch('data_fetcher.IQ_Option')
    def test_fetch_candles(self, MockIQOption):
        mock_iq = MockIQOption.return_value
        mock_iq.get_candles.return_value = [{'close': 1.1}, {'close': 1.2}, {'close': 1.3}]
        
        closes = data_fetcher.fetch_candles()
        self.assertEqual(len(closes), 3)
        self.assertEqual(closes[0], 1.1)

if __name__ == '__main__':
    unittest.main()
