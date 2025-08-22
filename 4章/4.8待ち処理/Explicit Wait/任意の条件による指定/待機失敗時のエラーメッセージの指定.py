from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

URL = "http://example.selenium.jp/reserveApp/"
WAIT_SECONDS = 10

with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)
    driver.get(URL)

    wait.until(lambda d: d.find_element(By.ID, "存在しないID"), message="存在しない")
