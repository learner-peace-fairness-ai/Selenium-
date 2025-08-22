from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "http://example.selenium.jp/reserveApp/"
WAIT_SECONDS = 10

with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)
    driver.get(URL)

    body = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print(body.value_of_css_property("background-color"))
