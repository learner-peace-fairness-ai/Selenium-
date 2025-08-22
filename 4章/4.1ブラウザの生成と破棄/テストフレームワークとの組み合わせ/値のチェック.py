import unittest
from unittest import TestCase

from selenium import webdriver


class SampleTest(TestCase):
    driver = None

    def setUp(self):
        global driver
        driver = webdriver.Edge()

    def tearDown(self):
        driver.quit()

    def test_ページのタイトルの取得が成功すること(self):
        URL = "http://example.selenium.jp/reserveApp/"
        expected = "予約情報入力"

        driver.get(URL)
        self.assertEqual(driver.title, expected)


if __name__ == "__main__":
    unittest.main()
