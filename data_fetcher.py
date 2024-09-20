# data_fetcher.py
import time
import numpy as np
from iqoptionapi.stable_api import IQ_Option
import config

def fetch_candles():
    iq = IQ_Option(config.IQ_OPTION_EMAIL, config.IQ_OPTION_PASSWORD)
    iq.connect()

    if iq.check_connect():
        print("Successfully connected to IQ Option API")
    else:
        print("Failed to connect to IQ Option API")
        return None

    # Fetch 1800 seconds (30 minutes) of 1-minute candles
    candles = iq.get_candles(config.SYMBOL, config.TIMEFRAME, config.CANDLE_COUNT, time.time())
    closes = np.array([candle['close'] for candle in candles])
    return closes
