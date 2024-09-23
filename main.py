from scraper.product_data_extractor import ScraperProductDataExtractor
from saver.json_data_saver import JSONDataSaver

name_js_file: str = 'mcdonalds.json'


def parse_and_save_data() -> None:
    mcdonalds: ScraperProductDataExtractor = ScraperProductDataExtractor(
        'https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html')
    mcdonalds.get_items_url()
    data = mcdonalds.collect_items_data()

    data_saver: JSONDataSaver = JSONDataSaver(name_js_file)
    data_saver.create_structured_data(data)
    data_saver.create_file()


if __name__ == "__main__":
    parse_and_save_data()
