# logger.py
import logging

def setup_logger(log_file='trading_bot.log', log_level=logging.INFO):
    # Create a custom logger
    logger = logging.getLogger(__name__)

    # Set the log level
    logger.setLevel(log_level)

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(log_file)

    # Set the log level for handlers
    c_handler.setLevel(log_level)
    f_handler.setLevel(log_level)

    # Create formatters and add them to handlers
    c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger
