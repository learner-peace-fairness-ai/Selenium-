from selenium import webdriver

URL = "https://www.google.co.jp/"
COOKIE_NAME = "my_cookie"

with webdriver.Edge() as driver:
    driver.get(URL)

    cookie = {"name": COOKIE_NAME, "value": "値"}
    driver.add_cookie(cookie)

    print(driver.get_cookie(COOKIE_NAME))
