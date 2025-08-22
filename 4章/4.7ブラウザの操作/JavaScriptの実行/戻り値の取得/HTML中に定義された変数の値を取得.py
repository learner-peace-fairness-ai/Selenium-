from pathlib import Path

from selenium import webdriver

HTML_FILE = Path("src.html").resolve()
URL = f"file://{HTML_FILE}"

with webdriver.Edge() as driver:
    driver.get(URL)

    val = driver.execute_script("return 'testValue';")
    print(val)
