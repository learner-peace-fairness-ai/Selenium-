from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "http://example.selenium.jp/reserveApp/"
WAIT_SECONDS = 10

with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)
    driver.get(URL)

    plan_a = wait.until(EC.element_to_be_clickable((By.NAME, "plan_a")))
    if not plan_a.is_selected():
        plan_a.click()

    if plan_a.is_selected():
        plan_a.click()
