from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

HTML_FILE = (Path.cwd() / "page.html").resolve()
URL = f"file://{HTML_FILE}"
WAIT_SECONDS = 10


def switch_to_title_window(driver, title):
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if title in driver.title:
            return

    raise Exception(f"「{title}」のウィンドウが見つかりません")


with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)

    driver.get(URL)
    original_handles = driver.window_handles
    print(driver.title)

    btn = wait.until(EC.element_to_be_clickable((By.ID, "openButton")))
    btn.click()
    wait.until(EC.new_window_is_opened(original_handles))

    switch_to_title_window(driver, "予約情報入力")

    print(driver.title)
    driver.close()

    switch_to_title_window(driver, "メイン")
    print(driver.title)
