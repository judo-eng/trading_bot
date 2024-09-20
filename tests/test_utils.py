
# tests/test_utils.py
import unittest
import numpy as np
import utils

class TestUtils(unittest.TestCase):

    def test_calculate_indicators(self):
        closes = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
        sma_3, sma_6, sma_14, macd, macdsignal = utils.calculate_indicators(closes)
        
        self.assertEqual(len(sma_3), len(closes))
        self.assertEqual(len(macd), len(closes))

if __name__ == '__main__':
    unittest.main()
