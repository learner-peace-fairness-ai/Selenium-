# file:///のアクセスでは<a>のリンククリックでダウンロードできないのでローカルサーバーを起動して実行する
#   プログラム実行前にローカルサーバーを起動
#       python -m http.server 8000
#   プログラム実行後にサーバーを停止
#       Ctrl + c
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

HTML_FILE = (Path.cwd() / "page.html").resolve()
DOWNLOAD_DIR = (Path.cwd() / "download").resolve()
URL = "http://localhost:8000/page.html"
WAIT_SECONDS = 10

options = Options()
prefs = {"download.default_directory": str(DOWNLOAD_DIR)}
options.add_experimental_option("prefs", prefs)

with webdriver.Edge(options=options) as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)

    driver.get(URL)

    download_link = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "a")))
    download_link.click()
