from selenium import webdriver

URL = "http://example.selenium.jp/reserveApp/"

with webdriver.Edge() as driver:
    driver.get(URL)
    position = driver.get_window_position()
    print(f"x: {position['x']}, y: {position['y']}")

    x = 100
    y = 200
    driver.set_window_position(x, y)
