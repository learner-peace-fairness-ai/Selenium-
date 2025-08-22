from selenium import webdriver

with webdriver.Firefox() as driver:
    driver.execute_script("window.prompt('入力してください', '初期値');")

    prompt = driver.switch_to.alert
    prompt.send_keys("abc")
    prompt.accept()
