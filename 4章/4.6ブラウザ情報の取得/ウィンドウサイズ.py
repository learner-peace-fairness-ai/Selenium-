from selenium import webdriver

URL = "http://example.selenium.jp/reserveApp/"

with webdriver.Edge() as driver:
    driver.get(URL)
    size = driver.get_window_size()
    print(f"width: {size['width']}, height: {size['height']}")

    x = 100
    y = 200
    driver.set_window_size(x, y)

    driver.maximize_window()
