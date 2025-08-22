from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

HTML_FILE = (Path.cwd() / "page1.html").resolve()
URL = f"file://{HTML_FILE}"
WAIT_SECONDS = 10


with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)

    driver.get(URL)
    print(driver.title)

    wait.until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe[name='sample1']")
        )
    )
    wait.until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe[name='sample2']")
        )
    )
    title = wait.until(EC.presence_of_element_located((By.TAG_NAME, "title")))
    print(title.get_attribute("textContent"))

    driver.switch_to.default_content()
    title = wait.until(EC.presence_of_element_located((By.TAG_NAME, "title")))
    print(title.get_attribute("textContent"))
