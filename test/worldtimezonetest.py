'''
Unit Testing for worldtimezone.py
'''
import unittest
from worldtimezone import print_time, load_json, set_logging, download_file

_CONFIG_FILE = './config/configuration.json'

class TestWorldTimeZone(unittest.TestCase):
    """Unit Test"""
    config_file = load_json(_CONFIG_FILE)
    url = config_file['url']
    dest = config_file['download_path']
    filename = config_file['filename']
    logger = set_logging(config_file['logfilename'], config_file['logformat'])

    def test_print_time_success(self):
        """
        Testing print_time() function for success
        """
        self.assertEqual(print_time("Asia/Kolkata", "india standard time", self.logger), 'Success')
    def test_print_time_fail(self):
        """
        Testing print_time() function for fail
        """
        self.assertEqual(print_time("Asia/KolkataABC", "india standard", self.logger), 'Fail')
    def test_download_file_success(self):
        """
        Testing download_file() function for success
        """
        self.assertEqual(download_file(self.url, self.dest, self.filename, self.logger), True)
        if __name__ == '__main__':
            unittest.main()
