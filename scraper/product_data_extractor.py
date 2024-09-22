import requests
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


class ScraperProductDataExtractor:

    def __init__(self, page_url):
        self.page_url = page_url
        self.domain_name = urlparse(page_url).scheme + '://' + urlparse(page_url).netloc
        self.items_url = []
        self.driver = None

    def _start_browser(self):
        service = Service()
        options = webdriver.FirefoxOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(service=service, options=options)

    def _quit_browser(self):
        self.driver.quit()

    def get_items_url(self):
        response = requests.get(self.page_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            menu_items = soup.find_all('li', class_='cmp-category__item')
            for menu_item in menu_items:
                self.items_url.append(self.domain_name + menu_item.find('a')['href'])
            return True
        print(f"Error: {response.status_code}")
        return False

    def get_item_html(self, item_url):
        self._start_browser()
        self.driver.get(item_url)
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        self._quit_browser()
        return soup

    def collect_item_data(self, item_url):
        soup = self.get_item_html(item_url)
        name = soup.find('span', class_='cmp-product-details-main__heading-title').text.strip()
        description = soup.find('div', class_='cmp-text').text.strip().replace('\xa0', ' ').replace('\n', '')
        calories_element, fats_element, carbs_element, proteins_element = soup.find_all('li',
                                                                                        class_='cmp-nutrition-summary__heading-primary-item')
        calories_value = calories_element.find('span', class_='sr-only sr-only-pd').text.strip().split('ккал')[0].strip()
        fats_value = fats_element.find('span', class_='value').text.strip().split('г')[0].strip()
        carbs_value = carbs_element.find('span', class_='value').text.strip().split('г')[0].strip()
        proteins_value = proteins_element.find('span', class_='value').text.strip().split('г')[0].strip()
        unsaturated_fats_element, sugar_element, salt_element, portion_element = soup.find_all('li',
                                                                                               class_='label-item')[0:4]
        unsaturated_fats_value = unsaturated_fats_element.find('span', class_='value').text.strip().split('г')[0]
        sugar_value = sugar_element.find('span', class_='value').text.strip().split('г')[0].strip()
        salt_value = salt_element.find('span', class_='value').text.strip().split('г')[0].strip()
        portion_value = portion_element.find('span', class_='value').text.strip().split('г')[0].strip()
        return [name, description, calories_value, fats_value, carbs_value, proteins_value, unsaturated_fats_value,
                sugar_value, salt_value, portion_value]

    def collect_items_data(self):
        data = [self.collect_item_data(item_url) for item_url in self.items_url]
        return data
