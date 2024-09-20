# executor.py
from iqoptionapi.stable_api import IQ_Option
import config

def execute_trade(signal):
    amount = 1  # Define the amount for the trade
    iq = IQ_Option(config.IQ_OPTION_EMAIL, config.IQ_OPTION_PASSWORD)
    iq.connect()

    if signal == 'call':
        iq.buy(amount, config.SYMBOL, "call", config.EXPIRATION_TIME)  # 3-minute expiration for a call option
    elif signal == 'put':
        iq.buy(amount, config.SYMBOL, "put", config.EXPIRATION_TIME)  # 3-minute expiration for a put option
