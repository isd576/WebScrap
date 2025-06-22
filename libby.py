import warnings

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

warnings.filterwarnings("ignore")

options=webdriver.FirefoxOptions()
service = Service(r"C:\Users\fizzy\Downloads\geckodriver-v0.36.0-win64\geckodriver.exe")

driver = webdriver.Firefox(service=service, options=options)

driver.get("https://libbyapp.com/search/nh")