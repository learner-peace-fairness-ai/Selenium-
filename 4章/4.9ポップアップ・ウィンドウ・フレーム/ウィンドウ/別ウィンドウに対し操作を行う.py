from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

HTML_FILE = (Path.cwd() / "page.html").resolve()
URL = f"file://{HTML_FILE}"
WAIT_SECONDS = 10

with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)

    driver.get(URL)
    existing_windows = driver.window_handles

    btn = wait.until(EC.element_to_be_clickable((By.ID, "openButton")))
    btn.click()
    wait.until(EC.new_window_is_opened(existing_windows))

    default_window = driver.current_window_handle
    new_window = driver.window_handles[-1]
    driver.switch_to.window(new_window)

    print(driver.title)
    driver.close()

    driver.switch_to.window(default_window)
    print(driver.title)
