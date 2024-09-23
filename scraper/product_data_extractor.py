import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from typing import List, Optional
from dto.product_dto import ProductDto


class ProductScraper:
    def __init__(self, page_url: str) -> None:
        self.menu_page_url: str = page_url
        self.domain_name: str = urlparse(page_url).scheme + '://' + urlparse(page_url).netloc
        self.items_url: List[str] = []
        self.driver: Optional[webdriver.Firefox] = None

    def _start_browser(self) -> None:
        service = Service()
        options = webdriver.FirefoxOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(service=service, options=options)

    def _quit_browser(self) -> None:
        if self.driver:
            self.driver.quit()

    def extract_item_urls(self) -> bool:
        response = requests.get(self.menu_page_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            menu_items = soup.find_all('li', class_='cmp-category__item')
            for menu_item in menu_items:
                self.items_url.append(self.domain_name + menu_item.find('a')['href'])
            return True
        print(f"Error: {response.status_code}")
        return False

    def fetch_item_html(self, item_url: str) -> Optional[BeautifulSoup]:
        retries: int = 0
        while retries < 5:
            self._start_browser()
            try:
                self.driver.get(item_url)
                self.driver.implicitly_wait(2)
                page_source: str = self.driver.page_source
                soup: BeautifulSoup = BeautifulSoup(page_source, 'html.parser')
                # Check that the data is loaded so that there are no breakdowns
                unsaturated_fats_element, sugar_element, salt_element, portion_element = soup.find_all('li',
                                                                                                       class_='label-item')[0:4]
                return soup
            except (ValueError, IndexError):
                retries += 1
                print(f"Error: Elements not found on {item_url}. Retrying... ({retries}/5)")
            finally:
                self._quit_browser()

        print(f"Failed to load required elements after 5 attempts: {item_url}")
        return None

    def extract_all_product_data(self, item_url: str) -> Optional[ProductDto]:
        soup: Optional[BeautifulSoup] = self.fetch_item_html(item_url)
        if soup is None:
            return None
        name: str = soup.find('span', class_='cmp-product-details-main__heading-title').text.strip()
        description: str = soup.find('div', class_='cmp-text').text.strip().replace('\xa0', ' ').replace('\n', '')
        calories_element, fats_element, carbs_element, proteins_element = soup.find_all('li',
                                                                                        class_='cmp-nutrition-summary__heading-primary-item')
        calories_value: str = calories_element.find('span', class_='sr-only sr-only-pd').text.strip().split('ккал')[
            0].strip()
        fats_value: str = fats_element.find('span', class_='value').text.strip().split('г')[0].strip()
        carbs_value: str = carbs_element.find('span', class_='value').text.strip().split('г')[0].strip()
        proteins_value: str = proteins_element.find('span', class_='value').text.strip().split('г')[0].strip()
        unsaturated_fats_element, sugar_element, salt_element, portion_element = soup.find_all('li',
                                                                                               class_='label-item')[0:4]
        unsaturated_fats_value: str = unsaturated_fats_element.find('span', class_='value').text.strip().split('г')[0]
        sugar_value: str = sugar_element.find('span', class_='value').text.strip().split('г')[0].strip()
        salt_value: str = salt_element.find('span', class_='value').text.strip().split('г')[0].strip()
        portion_value: str = portion_element.find('span', class_='value').text.strip().split('г')[0].strip()
        return ProductDto(
            name=name,
            description=description,
            calories=calories_value,
            fats = fats_value,
            carbs=carbs_value,
            proteins=proteins_value,
            unsaturated=unsaturated_fats_value,
            sugar=sugar_value,
            salt_value=salt_value,
            portion=portion_value
        )

    def collect_items_data(self) -> List[Optional[ProductDto]]:
        data: List[Optional[ProductDto]] = [self.extract_all_product_data(item_url) for item_url in self.items_url]
        return [item for item in data if item]
