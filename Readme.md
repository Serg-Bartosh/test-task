# Scraper and FlaskAPI Product Data Service

## Overview

This project consists of three main components:

1. **ScraperProductDataExtractor**: A class responsible for scraping product data from McDonald's website.
2. **JSONDataSaver**: A class for saving the scraped product data into a JSON file.
3. **FlaskAPI**: A RESTful API that provides endpoints for accessing the product data stored in the JSON file.

## Installation

### Step 1: Install Dependencies

Ensure you have all the necessary libraries installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Running the Project

**Step 1:** Run the Scraper

To start, run the scraping process which will extract product data from McDonald's website and save it into a JSON file.

**Step 2:** Launch the Flask API

Once the data has been successfully scraped and saved, you can start the Flask application by running the following
command:

```bash
flask --app views run
```

**Step 3:** Access the API

The Flask API will be available locally on http://127.0.0.1:5000. You can now interact with the available endpoints
through your browser or API client.
API Endpoints

Get All Products:
Endpoint: /all_products/
Description: Returns a list of all products.
Example: http://127.0.0.1:5000/all_products/

Get Product by Name:
Endpoint: /products/{product_name}
Description: Returns data for a specific product by its name.
Example: http://127.0.0.1:5000/products/BigMac

Get Specific Field of a Product:
Endpoint: /products/{product_name}/{field}
Description: Returns a specific field of a product.
Example: http://127.0.0.1:5000/products/BigMac/price
