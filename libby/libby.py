import warnings

from bs4 import BeautifulSoup
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


def check_availbility(bs):
    status = bs.find('div', class_='title-status')
    if status:
        stat = status.get('title')
        if stat and "Available to borrow" in stat:
            return True
    return False

def get_title(bs):
    title = bs.find('span', {'class' : 'title-tile-title'})
    return title

try:

    #searhing for the book - selenium
    search_input = WebDriverWait(driver, 15). until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type=search]")))
    search_input.click()
    search_input.send_keys("Ghost Roast")
    search_input.send_keys(Keys.RETURN)
    curl = driver.current_url
    
    #Wait for results to load
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "title-tile-biblio")))

    #soup time
    html = driver.page_source
    bs = BeautifulSoup(html, 'lxml')

    #title of first book
    titles = get_title(bs)
    print("Title: ", titles.text)

    #avalilbility
    availbe = check_availbility(bs)
    print("Avablie:", availbe)

except Exception as e:
    print("An error occures", e)
    driver.quit()