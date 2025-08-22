from unittest import TestCase

from selenium import webdriver


class SampleTest(TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Edge()

    @classmethod
    def tearDownClass(cls):
        driver.quit()

    def test_処理Aが成功すること(self):
        pass
