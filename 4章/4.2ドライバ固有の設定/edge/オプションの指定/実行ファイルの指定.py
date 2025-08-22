from selenium import webdriver
from selenium.webdriver.edge.service import Service

EDGE_DRIVER_PATH = "msedgedriver.exeのパス"

edge_service = Service(executable_path=EDGE_DRIVER_PATH)

with webdriver.Edge(service=edge_service) as driver:
    pass
