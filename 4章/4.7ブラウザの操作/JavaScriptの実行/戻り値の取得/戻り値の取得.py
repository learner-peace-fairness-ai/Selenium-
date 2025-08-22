from selenium import webdriver

URL = "http://example.selenium.jp/reserveApp/"

with webdriver.Edge() as driver:
    driver.get(URL)

    val = driver.execute_script("return 'test';")
    print(val)
