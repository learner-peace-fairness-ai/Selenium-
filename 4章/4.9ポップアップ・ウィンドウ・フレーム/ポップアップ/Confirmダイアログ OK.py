from selenium import webdriver

with webdriver.Edge() as driver:
    driver.execute_script("window.confirm('実行しますか？');")

    alert = driver.switch_to.alert
    alert.accept()
