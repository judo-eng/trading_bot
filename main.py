# main.py
import time
from strategy import trade_logic
import logger

def main():
    log = logger.setup_logger()
    log.info("Starting trading bot...")

    # Run the trade logic continuously
    while True:
        trade_logic()
        time.sleep(60)  # Wait for the next minute candle

if __name__ == "__main__":
    main()
