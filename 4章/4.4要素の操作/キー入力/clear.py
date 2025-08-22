from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://example.selenium.jp/reserveApp/"

with webdriver.Edge() as driver:
    driver.get(URL)

    name_field = driver.find_element(By.NAME, "gname")

    name_field.send_keys("abc")
    name_field.clear()
    name_field.send_keys("xyz")
