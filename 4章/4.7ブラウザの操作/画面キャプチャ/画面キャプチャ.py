from selenium import webdriver

URL = "http://example.selenium.jp/reserveApp/"

with webdriver.Edge() as driver:
    driver.get(URL)

    driver.save_screenshot("screenshot.png")

    binary_img = driver.get_screenshot_as_png()
    print(binary_img)

    str_img = driver.get_screenshot_as_base64()
    print(str_img)
