from operator import contains
from _logger import logger
from _config import config
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.parse import parse_qs, urlparse

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

    try:
        soup = BeautifulSoup(htmlstring, "lxml")
        a_item_list = soup.select("a")
        filtered_naver_a_item_list=filter(lambda x: "네이버" in x.text, a_item_list)
    except Exception as _e:
        logger.warn("Parsing HTML was failed : "+ str(_e))
    else:
        for a_item in filtered_naver_a_item_list:
            # https://stackoverflow.com/questions/5074803/retrieving-parameters-from-a-url
            parsed_url=urlparse(a_item['href'])
            no = parse_qs(parsed_url.query)['no'][0]
            title = a_item.text
            link = "/".join([DOMAIN_DIR_URL, a_item['href']])
            result_item = {
                "no": no,
                "title": title,
                "link": link
            }
            logger.debug("Appending...{}".format(result_item))
            result_list.append(result_item)
    finally:
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
