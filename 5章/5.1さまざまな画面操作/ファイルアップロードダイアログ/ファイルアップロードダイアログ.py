from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

HTML_FILE = (Path.cwd() / "page.html").resolve()
UPLOAD_FILE = (Path.cwd() / "sample.txt").resolve()
URL = f"file://{HTML_FILE}"
WAIT_SECONDS = 10

with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)

    driver.get(URL)

    file_selector = wait.until(EC.element_to_be_clickable((By.ID, "file_upload")))
    file_selector.send_keys(str(UPLOAD_FILE))
