import requests
from urllib.parse import urlparse

from bs4 import BeautifulSoup


class ScraperProductDataExtractor:

    def __init__(self, site_url):
        self.site_url = site_url
        self.domain_name = urlparse(site_url).scheme+'://' + urlparse(site_url).netloc
        self.items_url = []
