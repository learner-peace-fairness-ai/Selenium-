from pathlib import Path

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

HTML_FILE = (Path.cwd() / "page.html").resolve()
URL = f"file://{HTML_FILE}"
WAIT_SECONDS = 10


with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)

    driver.get(URL)
    head = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='item1']"))
    )
    tail = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='item5']"))
    )

    actions = ActionChains(driver)
    actions.key_down(Keys.SHIFT).click(head).click(tail).key_up(Keys.SHIFT).perform()
