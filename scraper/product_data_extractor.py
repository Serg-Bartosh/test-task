import requests
from urllib.parse import urlparse

from bs4 import BeautifulSoup


class ScraperProductDataExtractor:

    def __init__(self, site_url):
        self.site_url = site_url
        self.domain_name = urlparse(site_url).scheme + '://' + urlparse(site_url).netloc
        self.items_url = []

    def get_items_url(self):
        response = requests.get(self.site_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            menu_items = soup.find_all('li', class_='cmp-category__item')
            for menu_item in menu_items:
                self.items_url.append(self.domain_name + menu_item.find('a')['href'])
        else:
            print(f"Ошибка при получении страницы: {response.status_code}")
