import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.goodreads.com/review/list/66610129-izzy?ref=nav_mybooks&shelf=to-read"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html5lib')

def get_title(soup):
    book = soup.find('a', class_='bookTitle')
    if book:
        book_title = book.text.strip()
        return book_title
    else:
        return ""
    
def get_author(soup):
    author = soup.find('author').text

def get_isbn(soup):
    isbn = soup.find('isbn').text

