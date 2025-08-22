from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

HTML_FILE = (Path.cwd() / "src.html").resolve()
URL = f"file://{HTML_FILE}"
WAIT_SECONDS = 10

with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)
    driver.get(URL)

    select = Select(wait.until(EC.element_to_be_clickable((By.NAME, "lang"))))
    select.select_by_value("ja")
    select.select_by_visible_text("英語")
    select.select_by_index(2)

    select.deselect_all()

    select.select_by_value("ja")
    select.deselect_by_value("ja")

    select.select_by_visible_text("英語")
    select.deselect_by_visible_text("英語")

    select.select_by_index(2)
    select.deselect_by_index(2)
