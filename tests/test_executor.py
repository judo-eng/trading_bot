
# tests/test_executor.py
import unittest
from unittest.mock import patch
import executor

class TestExecutor(unittest.TestCase):

    @patch('executor.IQ_Option')
    def test_execute_trade(self, MockIQOption):
        mock_iq = MockIQOption.return_value
        mock_iq.buy.return_value = (True, 'order_id')
        
        status, order_id = executor.execute_trade('call')
        self.assertTrue(status)
        self.assertEqual(order_id, 'order_id')

if __name__ == '__main__':
    unittest.main()
