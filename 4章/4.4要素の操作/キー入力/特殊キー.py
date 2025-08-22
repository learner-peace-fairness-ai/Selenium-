from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "http://example.selenium.jp/reserveApp/"

with webdriver.Edge() as driver:
    driver.get(URL)

    year_field = driver.find_element(By.NAME, "reserve_y")
    year_field.send_keys(Keys.TAB)

    month_field = driver.find_element(By.NAME, "reserve_m")
    month_field.send_keys(Keys.BACK_SPACE)

    name_field = driver.find_element(By.NAME, "gname")
    name_field.send_keys(Keys.ENTER)
