import warnings

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
warnings.filterwarnings("ignore")

options=webdriver.FirefoxOptions()
service = Service(r"C:\Users\fizzy\Downloads\geckodriver-v0.36.0-win64\geckodriver.exe")

driver = webdriver.Firefox(service=service, options=options)

driver.get("https://libbyapp.com/search/nh")



try:
    search_input = WebDriverWait(driver, 15). until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type=search]")))
    search_input.click()
    search_input.send_keys("Little Women")
    search_input.send_keys(Keys.RETURN)
except Exception as e:
    print("Search bar not found", e)
    driver.quit()