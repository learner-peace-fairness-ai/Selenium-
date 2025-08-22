from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://example.selenium.jp/reserveApp/"

with webdriver.Edge() as driver:
    driver.get(URL)

    input_tags = driver.find_elements(By.TAG_NAME, "input")
    print(len(input_tags))
