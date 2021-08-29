from logging.handlers import RotatingFileHandler
import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(levelname)5s | %(funcName)s() %(filename)s:%(lineno)d | %(message)s")

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_handler.setFormatter(formatter)

file_handler = RotatingFileHandler('logs.log', maxBytes=1024*1024, backupCount=1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)


if __name__ == "__main__":
    logger.info("stdout Loghandler is created")
    logger.debug("file loghandler is created")
    logger.error("Run python main.py, instead")