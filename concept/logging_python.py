import logging

logging.basicConfig(level=logging.DEBUG)
logging.info("ApplicationStarted")
logging.warning("Something unexpected happend")
logging.error("Ar error occured")
logging.critical("critical failure!")