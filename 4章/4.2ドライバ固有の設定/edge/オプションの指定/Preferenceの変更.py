from selenium import webdriver
from selenium.webdriver.edge.options import Options

DOWNLOAD_FOLDER_PATH = "ダウンロードフォルダの絶対パス"

edge_options = Options()
edge_options.add_experimental_option(
    "prefs",
    {
        "download.default_directory": DOWNLOAD_FOLDER_PATH,
    },
)

with webdriver.Edge(options=edge_options) as driver:
    pass
