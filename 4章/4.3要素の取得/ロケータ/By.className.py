from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "http://example.selenium.jp/reserveApp/"

with webdriver.Edge() as driver:
    driver.get(URL)

    btn = driver.find_element(By.CLASS_NAME, "btn")
    btn.send_keys(Keys.ENTER)
