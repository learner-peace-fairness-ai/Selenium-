from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

HTML_FILE = (Path.cwd() / "src.html").resolve()
URL = f"file://{HTML_FILE}"
WAIT_SECONDS = 10

with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)
    driver.get(URL)

    check_item = wait.until(EC.presence_of_element_located((By.NAME, "a")))
    print(check_item.is_selected())

    radio_item = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='radio'][value='on']")
        )
    )
    print(radio_item.is_selected())

    select_item = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "select[name='lang'] option[value='ja']")
        )
    )
    print(select_item.is_selected())
