# Scraper and FastAPI Product Data Service

## Description

This project includes:
1. **ScraperProductDataExtractor** — a class for scraping product data from McDonald's website.
2. **JSONDataSaver** — a class for saving product data into a JSON file.
3. **FastAPI Application** — provides an API for working with product data stored in the JSON file.

## Installation and Setup

### 1. Installing Dependencies

Before starting, make sure all necessary libraries are installed. You can install them using `pip`:

```bash
pip install -r requirements.txt
```

## 2. Start project

### 1. Run project
### 2. Wait until the data is loaded and saved
### 3. Paste ```flask --app views run``` to terminal
### 4. Then you can go to the browser on localhost and use endpoints

#### Endpoints
##### 1. http://127.0.0.1:5000/all_products/ - will show u all products
##### 2. http://127.0.0.1:5000/products/{product_name} - will show u product with name = product_name
##### 3. http://127.0.0.1:5000/products/{product_name}/{fiel} - will show you the field of the selected product
