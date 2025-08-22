import time

from selenium import webdriver

URL = "http://example.selenium.jp/reserveApp/"

with webdriver.Edge() as driver:
    driver.get(URL)

    driver.back()
    driver.forward()
    driver.refresh()
