from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

URL = "http://example.selenium.jp/reserveApp/"
WAIT_SECONDS = 10


class TextInElement:
    def __init__(self, locator, text):
        self.locator = locator
        self.text = text

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        return self.text in element.text


with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)
    driver.get(URL)

    BUTTON_ID = "goto_next"
    LOCATOR = (By.ID, BUTTON_ID)
    TEXT = "次へ"
    wait.until(TextInElement(LOCATOR, TEXT))
    btn = driver.find_element(By.ID, BUTTON_ID)
    print(btn.text)
