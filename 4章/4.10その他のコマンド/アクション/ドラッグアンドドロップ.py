from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "http://example.selenium.jp/reserveApp"
WAIT_SECONDS = 10


with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)

    driver.get(URL)
    link = wait.until(
        EC.visibility_of_element_located((By.LINK_TEXT, "各プランの詳細"))
    )
    input_box = wait.until(EC.visibility_of_element_located((By.ID, "guestname")))

    actions = ActionChains(driver)
    actions.drag_and_drop(link, input_box).perform()
