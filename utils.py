# utils.py
import talib
import numpy as np

def calculate_indicators(closes):
    sma_3 = talib.SMA(closes, timeperiod=3)
    sma_6 = talib.SMA(closes, timeperiod=6)
    sma_14 = talib.SMA(closes, timeperiod=14)
    macd, macdsignal, macdhist = talib.MACD(closes, fastperiod=12, slowperiod=26, signalperiod=9)
    
    return sma_3, sma_6, sma_14, macd, macdsignal
