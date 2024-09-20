# tests/test_strategy.py
import unittest
from unittest.mock import patch
import strategy
import utils

class TestStrategy(unittest.TestCase):

    @patch('strategy.fetch_candles')
    @patch('strategy.utils.calculate_indicators')
    @patch('strategy.execute_trade')
    def test_trade_logic(self, mock_execute_trade, mock_calculate_indicators, mock_fetch_candles):
        mock_fetch_candles.return_value = [1.1, 1.2, 1.3]
        mock_calculate_indicators.return_value = ([1.1, 1.2, 1.3], [1.1, 1.2, 1.3], [1.1, 1.2, 1.3], [1.1, 1.2, 1.3], [1.1, 1.2, 1.3])
        
        strategy.trade_logic()
        mock_execute_trade.assert_called()

if __name__ == '__main__':
    unittest.main()
