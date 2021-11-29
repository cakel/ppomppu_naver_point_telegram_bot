from logging.handlers import RotatingFileHandler
import logging
import os
import sys
import gzip

def namer(name):
    return name + ".gz"

def rotator(source, dest):
    with open(source, "rb") as sf:
        data = sf.read()
        compressed = gzip.compress(data)
        with open(dest, "wb") as df:
            df.write(compressed)
    os.remove(source)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(levelname)5s | %(funcName)s() %(filename)s:%(lineno)d | %(message)s")

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_handler.setFormatter(formatter)

file_handler = RotatingFileHandler('logs.log', maxBytes=1024*1024*4, backupCount=5)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
file_handler.rotator = rotator
file_handler.namer = namer


logger.addHandler(file_handler)
logger.addHandler(stdout_handler)


if __name__ == "__main__":
    logger.info("stdout Loghandler is created")
    logger.debug("file loghandler is created")
    logger.error("Run python main.py, instead")
