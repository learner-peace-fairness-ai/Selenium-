from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://example.selenium.jp/reserveApp/"

with webdriver.Edge() as driver:
    driver.get(URL)

    form = driver.find_element(By.ID, "reserve_info")
    link = form.find_element(By.XPATH, ".//a[text()='各プランの詳細']")
    link.click()
