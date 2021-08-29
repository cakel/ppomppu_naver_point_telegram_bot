import telepot
import time
from telepot.loop import MessageLoop
from _config import config
from _logger import logger

chat_id_list = eval(config["TELEGRAM_DEFAULT_CHAT_ID"])
bot = telepot.Bot(config["TELEGRAM_TOKEN"])


def initialize_listening():
    MessageLoop(bot, handle).run_as_thread()

    if chat_id_list is not None and \
            isinstance(chat_id_list, list) and \
            chat_id_list != []:
        for chat_id in chat_id_list:
            bot.sendMessage(chat_id, "Bot is rebooted...")

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if chat_id in chat_id_list and \
            msg is not None and \
            'text' in msg.keys() and \
            msg['text'] == 'quit':
        bot.sendMessage(
            chat_id, "...Unsubscribed... To subscribe, type anything")
        chat_id_list.remove(chat_id)
    else:
        chat_id_list.append(chat_id)
        bot.sendMessage(
            chat_id, "...Subscribed... To unsubscribe, type 'quit'")
    logger.info(str(msg))


def send_message_from_result_list(result_list):
    for result_item in result_list:
        send_message(result_item["no"],
                     result_item["title"], result_item["link"])
    return


def send_message(no, title, link):
    for chat_id in chat_id_list:
        msg = "{} / {} / {}".format(no, title, link)
        title = title.replace("[", "")
        title = title.replace("]", "")
        title = title.replace("(", "")
        title = title.replace(")", "")
        msg_markdown = "No: {} [{}]({})".format(no, title, link)
        logger.info("Send msg:'{}' to chat_id: {}".format(msg, chat_id))
        bot.sendMessage(chat_id, msg_markdown, parse_mode="Markdown")


if __name__ == "__main__":
    # Keep the program running.
    MessageLoop(bot, handle).run_as_thread()
    logger.info('Telegram working only, on listening...')
    logger.warn("For working expectedly, run python main.py, instead")
    while 1:
        time.sleep(10)
