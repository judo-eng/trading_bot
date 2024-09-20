# strategy.py
import utils
from executor import execute_trade
from data_fetcher import fetch_candles

def trade_logic():
    closes = fetch_candles()
    if closes is None:
        return

    sma_3, sma_6, sma_14, macd, macdsignal = utils.calculate_indicators(closes)
    
    # Check if the last crossover conditions are met
    if sma_3[-1] > sma_6[-1] and sma_3[-1] > sma_14[-1] and macd[-1] > macdsignal[-1]:
        print("Bullish signal: Executing Call Option")
        execute_trade('call')
        
    elif sma_3[-1] < sma_6[-1] and sma_3[-1] < sma_14[-1] and macd[-1] < macdsignal[-1]:
        print("Bearish signal: Executing Put Option")
        execute_trade('put')
