from scraper.product_data_extractor import ProductScraper
from saver.json_data_saver import JSONDataSaver

name_js_file: str = 'mcdonalds.json'


def scrape_and_save_menu_data() -> None:
    mcdonalds: ProductScraper = ProductScraper(
        'https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html')
    mcdonalds.extract_item_urls()
    data = mcdonalds.collect_items_data()

    data_saver: JSONDataSaver = JSONDataSaver(name_js_file)
    data_saver.create_structured_data(data)
    data_saver.create_file()


if __name__ == "__main__":
    scrape_and_save_menu_data()
