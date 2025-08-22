from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

URL = "http://example.selenium.jp/reserveApp/"
WAIT_SECONDS = 10
POLLING_SECONDS = 1

with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS, poll_frequency=POLLING_SECONDS)
    driver.get(URL)

    BUTTON_ID = "goto_next"
    wait.until(lambda d: "次へ" in d.find_element(By.ID, BUTTON_ID).text)
    btn = driver.find_element(By.ID, BUTTON_ID)
    print(btn.text)
