from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from selenium import webdriver
from selenium.webdriver.common.by import By

url = urlopen("https://www.goodreads.com/review/list/190540906-test?shelf=to-read")
bs = BeautifulSoup(url.read(), 'lxml')
driver = webdriver.Chrome(executable_path='/')

def book_info():
    rows = bs.find_all('tr', {'class' : 'bookalike review'})
    for row in rows:
        title_id = row.find('td', {'class' : 'field title'})
        author_id = row.find('td', {'class' : 'field author'})
        if title_id and author_id:
            title = title_id.get_text(strip=True)
            author = author_id.get_text(strip=True)
            print(f"{title} -- {author}")
book_info()