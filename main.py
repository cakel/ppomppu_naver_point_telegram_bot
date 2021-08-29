from _logger import logger
from _file import save_db_to_file, load_db_from_file
from _url import fetch_html_to_string, get_record_list_info_from_html, get_sending_list_from_record
from _config import config
from _message import send_message_from_result_list, initialize_listening
from time import sleep

def mainloop():
    existing_result = []
    retrieved_result = []
    to_be_saved_result = []
    sending_target_list = []
    ret = ""

    while True:
        to_be_saved_result = []
        ret = fetch_html_to_string(config["FULL_URL"])
        existing_result = load_db_from_file()
        logger.info("Load from DB Item : {}".format(len(existing_result)))

        retrieved_result = get_record_list_info_from_html(ret)
        logger.info("Retrived from URL Item : {}".format(len(retrieved_result)))

        sending_target_list = get_sending_list_from_record(
            existing_result, retrieved_result)
        logger.info("New and Sending to Message Item : {}".format(
            len(sending_target_list)))
        to_be_saved_result.extend(sending_target_list)
        to_be_saved_result.extend(existing_result)

        '''
        Sending New Items for Telegram
        '''
        send_message_from_result_list(sending_target_list)

        logger.info("Save to DB Item : {}".format(len(sending_target_list)))
        save_db_to_file(database=to_be_saved_result)

        sleep(10) # 10 Second

if __name__ == "__main__":
    initialize_listening()
    mainloop()
    pass
