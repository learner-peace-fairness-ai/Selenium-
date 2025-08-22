from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "http://example.selenium.jp/reserveApp/"

with webdriver.Edge() as driver:
    driver.get(URL)

    name_field = driver.find_element(By.NAME, "gname")
    name_field.send_keys("ABC", Keys.BACK_SPACE)
