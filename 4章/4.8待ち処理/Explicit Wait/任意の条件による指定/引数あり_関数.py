from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

URL = "http://example.selenium.jp/reserveApp/"
WAIT_SECONDS = 10


def has_text(locator, text):
    return lambda d: text in d.find_element(*locator).text


with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)
    driver.get(URL)

    BUTTON_ID = "goto_next"
    LOCATOR = (By.ID, BUTTON_ID)
    TEXT = "次へ"
    wait.until(has_text(LOCATOR, TEXT))
    btn = driver.find_element(By.ID, BUTTON_ID)
    print(btn.text)
