from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "http://example.selenium.jp/reserveApp/"
WAIT_SECONDS = 10

with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)

    driver.get(URL)

    name_input_tag = wait.until(EC.visibility_of_element_located((By.ID, "guestname")))
    name_input_tag.send_keys("サンプルユーザ")

    next_btn = wait.until(EC.element_to_be_clickable((By.ID, "goto_next")))
    next_btn.click()
