from selenium import webdriver

with webdriver.Edge() as driver:
    driver.execute_script("window.alert('テスト');")

    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
