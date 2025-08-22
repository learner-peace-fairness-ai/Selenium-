from selenium import webdriver
from selenium.webdriver.edge.options import Options

edge_options = Options()
edge_options.add_argument("--inprivate")

with webdriver.Edge(options=edge_options) as driver:
    pass
