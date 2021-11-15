from _logger import logger
from _config import config
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def fetch_html_to_string(urlstring: None) -> str:
    ua = UserAgent()
    retString = ""
    if urlstring is None:
        urlstring = config["FULL_URL"]

    header = {'User-Agent': str(ua.chrome)}
    try:
        ret = requests.get(urlstring, headers=header)
        retString = str(ret.text)
    except Exception as e:
        logger.error("{}".format(e))
    else:
        logger.debug("Fetched {}".format(urlstring))

    return retString


def get_record_list_info_from_html(htmlstring: str) -> list:
    DOMAIN_DIR_URL = "/".join(config["FULL_URL"].split("/")[:-1])

    title = ''
    link = ''
    no = 0
    result_item = {}
    result_list = []

    soup = BeautifulSoup(htmlstring, "lxml")
    table_tr_list = soup.find(id="revolution_main_table").find_all("tr")
    for table_tr_item in table_tr_list:
        record_item = table_tr_item.find_all("td")

        try:
            if len(record_item) > 4 and \
                    len(record_item[3].contents) > 4 and \
                    len(record_item[3].contents[3]) > 0:
                title = record_item[3].contents[3].text
                link = "{}/{}".format(DOMAIN_DIR_URL,
                                      (record_item[3].contents[3].attrs['href']))
                no = link.split("no=")[1]
                if "네이버" in title:
                    result_item = {
                        "no": no,
                        "title": title,
                        "link": link
                    }
                    logger.debug("Appending...{}".format(result_item))
                    result_list.append(result_item)
        except Exception as e:
            logger.warning(e)

    return result_list

def get_sending_list_from_record(existing_result_list, retrieved_result_list):
    '''
        In case of sent "True" and "False" combination list,
        Filtering out that sent is "True" and removing duplication
    '''
    result_list = []
    existing_no_list = []

    for existing_result_item in existing_result_list:
        existing_no_list.append(existing_result_item["no"])

    for retrieved_result_item in retrieved_result_list:
        if retrieved_result_item["no"] not in existing_no_list:
            logger.debug("Appending New item... {}".format(retrieved_result_item))
            result_list.append(retrieved_result_item)

    return result_list

if __name__ == "__main__":
    logger.info("No user interaction is allowed")
    logger.error("Run python main.py, instead")
