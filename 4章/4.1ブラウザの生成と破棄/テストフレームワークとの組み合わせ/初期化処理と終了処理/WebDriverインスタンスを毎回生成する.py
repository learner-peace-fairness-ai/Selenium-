from unittest import TestCase

from selenium import webdriver


class SampleTest(TestCase):
    driver = None

    def setUp(self):
        global driver
        driver = webdriver.Edge()

    def tearDown(self):
        driver.quit()

    def test_処理Aが成功すること(self):
        pass

    def test_処理Bが成功すること(self):
        pass
