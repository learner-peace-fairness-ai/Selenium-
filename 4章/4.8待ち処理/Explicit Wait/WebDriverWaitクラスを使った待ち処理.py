from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "http://example.selenium.jp/reserveApp/"
WAIT_SECONDS = 10

with webdriver.Edge() as driver:
    driver.get(URL)

    wait = WebDriverWait(driver, WAIT_SECONDS)
    wait.until(EC.visibility_of_element_located((By.NAME, "gname")))
