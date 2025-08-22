from pathlib import Path

from selenium import webdriver

HTML_FILE = Path("src.html").resolve()
URL = f"file://{HTML_FILE}"

with webdriver.Edge() as driver:
    driver.get(URL)

    driver.execute_script("window.alert(arguments[0]);", "Hello world!")
