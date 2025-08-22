from selenium import webdriver
from selenium.webdriver.edge.options import Options

EXTENSION_PATH = "拡張機能のフォルダ/バージョンのパス"

edge_options = Options()
edge_options.add_argument(f"--load-extension={EXTENSION_PATH}")

with webdriver.Edge(options=edge_options) as driver:
    pass
