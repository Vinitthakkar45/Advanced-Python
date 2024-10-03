import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("This is a debuggin msg")
logging.info("This is an informational message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")