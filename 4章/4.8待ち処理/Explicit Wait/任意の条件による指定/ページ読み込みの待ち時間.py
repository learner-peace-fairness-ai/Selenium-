from selenium import webdriver

URL = "http://example.selenium.jp/reserveApp/"

with webdriver.Edge() as driver:
    driver.set_page_load_timeout(10)

    driver.get(URL)
