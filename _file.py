import json
from _logger import logger

def save_db_to_file(database, filename="db.json", encoding='UTF-8-sig') -> None:
    try:
        with open(filename, 'w') as outfile:
            json.dump(database, outfile, ensure_ascii=False, indent=4)
            logger.debug(f"Save DB to {filename}")
    except Exception as e:
        logger.error(e)
    return


def load_db_from_file(filename='db.json') -> object:
    database = []
    try:
        with open(filename) as json_file:
            database = json.load(json_file)
            logger.debug(f"Load DB from {filename}")
    except Exception as e:
        logger.error(e)

    return database

if __name__ == "__main__":
    logger.info("No user interaction is allowed")
    logger.error("Run python main.py, instead")