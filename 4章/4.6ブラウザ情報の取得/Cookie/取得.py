from selenium import webdriver

URL = "https://www.google.co.jp/"

with webdriver.Edge() as driver:
    driver.get(URL)

    cookies = driver.get_cookies()
    for cookie in cookies:
        for key, val in cookie.items():
            print(f"{key}: {val}")

    cookie_name = "NID"
    print(driver.get_cookie(cookie_name))
