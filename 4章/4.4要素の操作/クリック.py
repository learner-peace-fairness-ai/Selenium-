from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://example.selenium.jp/reserveApp/"

with webdriver.Edge() as driver:
    driver.get(URL)

    link = driver.find_element(By.LINK_TEXT, "各プランの詳細")
    link.click()
