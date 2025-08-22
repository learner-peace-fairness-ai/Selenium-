from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://example.selenium.jp/reserveApp/"
WAIT_SECONDS = 10

with webdriver.Edge() as driver:
    driver.get(URL)

    eixits = bool(driver.find_elements(By.ID, "goto_next"))
    print(eixits)
