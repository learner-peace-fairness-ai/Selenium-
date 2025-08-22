from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.event_firing_webdriver import AbstractEventListener
from selenium.webdriver.support.wait import WebDriverWait


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(f"要素取得: {by}: {value}")

    def before_click(self, element, driver):
        print("クリック")


URL = "http://example.selenium.jp/reserveApp"
WAIT_SECONDS = 10

with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)

    driver.get(URL)
    wait.until(EC.element_to_be_clickable((By.ID, "goto_next")))

    ef_driver = EventFiringWebDriver(driver, MyListener())
    btn = ef_driver.find_element(By.ID, "goto_next")
    btn.click()
