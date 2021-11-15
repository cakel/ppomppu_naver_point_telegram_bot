from logging.handlers import RotatingFileHandler
import logging
import sys

class GZipRotator:
    def __call__(self, source, dest):
        os.rename(source, dest)
        f_in = open(dest, 'rb')
        f_out = gzip.open("%s.gz" % dest, 'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()
        os.remove(dest)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(levelname)5s | %(funcName)s() %(filename)s:%(lineno)d | %(message)s")

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_handler.setFormatter(formatter)

file_handler = RotatingFileHandler('logs.log', maxBytes=1024*1024*4, backupCount=5)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
file_handler.rotator = GZipRotator()

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)


if __name__ == "__main__":
    logger.info("stdout Loghandler is created")
    logger.debug("file loghandler is created")
    logger.error("Run python main.py, instead")
