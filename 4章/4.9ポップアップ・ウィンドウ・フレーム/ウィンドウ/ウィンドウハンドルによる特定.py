from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

HTML_FILE = (Path.cwd() / "page.html").resolve()
URL = f"file://{HTML_FILE}"
WAIT_SECONDS = 10


def get_new_window_handle(handles_before_open, handles_after_open):
    handles = [x for x in handles_after_open if x not in handles_before_open]

    if len(handles) == 0:
        raise Exception("新しいウィンドウが見つかりません")
    elif len(handles) >= 2:
        raise Exception("新しいウィンドウが複数あります")
    else:
        return handles[0]


with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)

    driver.get(URL)
    original_handles = driver.window_handles
    original_handle = driver.current_window_handle

    btn = wait.until(EC.element_to_be_clickable((By.ID, "openButton")))
    btn.click()
    wait.until(EC.new_window_is_opened(original_handles))
    new_handles = driver.window_handles

    new_handle = get_new_window_handle(original_handles, new_handles)
    driver.switch_to.window(new_handle)

    print(driver.title)
    driver.close()

    driver.switch_to.window(original_handle)
    print(driver.title)
