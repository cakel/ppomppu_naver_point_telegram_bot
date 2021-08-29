import unittest
import os
import json
from unittest.mock import patch
from _url import get_sending_list_from_record, fetch_html_to_string, get_record_list_info_from_html
from _file import load_db_from_file, save_db_to_file


class TestSuite(unittest.TestCase):

    def test_save_and_load(self):
        DB_DUMMY_LIST = []
        DB_TEST_LIST = []
        DB_DUMMY1 = {
            "no": 1,
            "link": "http",
            "title": "2021-08-29",
            "sent": False
        }
        DB_DUMMY2 = {
            "no": 2,
            "link": "http",
            "title": "2021-08-29",
            "sent": False
        }
        DB_DUMMY_LIST.append(DB_DUMMY1)
        DB_DUMMY_LIST.append(DB_DUMMY2)

        save_db_to_file(DB_DUMMY_LIST, "_db.json")
        DB_TEST_LIST = load_db_from_file("_db.json")

        self.assertTrue(DB_TEST_LIST == DB_DUMMY_LIST)

        if os.path.exists("_db.json"):
            os.remove("_db.json")

    @patch('requests.get')
    def test_fetch_string_from_url(self, test_patch):
        class dummy_result():
            text = "TEST"
        test_patch.return_value = dummy_result()
        ret = fetch_html_to_string(None)
        self.assertTrue(ret == "TEST")
        pass

    def test_get_record_list_info_from_html(self):
        with open("./_test/test_get_record_list_info_from_html_in.txt", "r", encoding='utf-8') as readInFile:
            with open("./_test/test_get_record_list_info_from_html_out.txt", "r", encoding='utf-8') as readOutFile:
                actual_result = str(
                    get_record_list_info_from_html(readInFile.read()))
                expect_result = str(json.load(readOutFile))
                self.assertTrue(actual_result == expect_result)
        pass

    def test_get_sending_list_from_record(self):
        existing_result_list = [
            {
                "no": "71339",
                "title": "[네이버페이] 참존 스토어찜 80원",
                "link": "https://www.ppomppu.co.kr/zboard/view.php?id=coupon&page=1&divpage=13&search_type=subject&keyword=%B3%D7%C0%CC%B9%F6&no=71339"
            }
        ]
        retrieved_result_list = [
            {
                "no": "71345",
                "title": "[네이버페이] 캐롯손해보험 20원 받으세요",
                "link": "https://www.ppomppu.co.kr/zboard/view.php?id=coupon&page=1&divpage=13&search_type=subject&keyword=%B3%D7%C0%CC%B9%F6&no=71345"
            },
            {
                "no": "71339",
                "title": "[네이버페이] 참존 스토어찜 80원",
                "link": "https://www.ppomppu.co.kr/zboard/view.php?id=coupon&page=1&divpage=13&search_type=subject&keyword=%B3%D7%C0%CC%B9%F6&no=71339"
            }
        ]
        expect_result = [{
            "no": "71345",
            "title": "[네이버페이] 캐롯손해보험 20원 받으세요",
            "link": "https://www.ppomppu.co.kr/zboard/view.php?id=coupon&page=1&divpage=13&search_type=subject&keyword=%B3%D7%C0%CC%B9%F6&no=71345"
        }]
        actual_result = get_sending_list_from_record(
            existing_result_list, retrieved_result_list)
        self.assertTrue(actual_result == expect_result)
        pass


if __name__ == '__main__':
    unittest.main()
