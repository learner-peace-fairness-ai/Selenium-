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

    breakfast_off_option = wait.until(
        EC.element_to_be_clickable((By.ID, "breakfast_off"))
    )

    actions = ActionChains(driver)
    actions.double_click(breakfast_off_option).perform()
