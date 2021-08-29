from _logger import logger
from dotenv import dotenv_values

config = dotenv_values(".env")

if __name__ == "__main__":
    logger.info("[Loaded Config]\n{}".format(config))
    logger.error("Run python main.py, instead")
