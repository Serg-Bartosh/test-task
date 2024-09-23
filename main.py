import uvicorn

from scraper.product_data_extractor import ScraperProductDataExtractor
from saver.json_data_saver import JSONDataSaver

mcdonalds = ScraperProductDataExtractor('https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html')
mcdonalds.get_items_url()
data = mcdonalds.collect_items_data()

name_js_file = 'mcdonalds.json'

data_saver = JSONDataSaver(name_js_file)
data_saver.create_structured_data(data)
data_saver.create_file()

if __name__ == "__main__":
    uvicorn.run("views:app", host="127.0.0.1", port=8001, reload=True)
