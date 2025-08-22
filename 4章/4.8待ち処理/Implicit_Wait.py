from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://example.selenium.jp/reserveApp/"
WAIT_SECONDS = 10

with webdriver.Edge() as driver:
    driver.get(URL)

    driver.implicitly_wait(WAIT_SECONDS)

    btn = driver.find_element(By.ID, "goto_next")
    print(btn.text)
