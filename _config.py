from _logger import logger
from dotenv import dotenv_values
import os

path_to_read = ".env" if os.path.exists(".env") else "config.env"
config = dotenv_values(path_to_read)

if __name__ == "__main__":
    logger.info("[Loaded Config]\n{}".format(config))
    logger.error("Run python main.py, instead")
