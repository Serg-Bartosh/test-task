import json
from fastapi import FastAPI, HTTPException
from urllib.parse import unquote

app = FastAPI()


def load_products_from_file(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_path}.")
        return {}


products = load_products_from_file('saver/mc_data.json')


def find_product_by_name(product_name: str):
    for product in products:
        if product['name'].lower() == product_name.lower():
            return product
    return None


@app.get("/all_products/")
def get_all_products():
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products


@app.get("/products/{product_name}")
def get_product(product_name: str):
    product_name = unquote(product_name)
    product = find_product_by_name(product_name)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.get("/products/{product_name}/{product_field}")
def get_product_field(product_name: str, product_field: str):
    product_name = unquote(product_name)
    product = find_product_by_name(product_name)
    product_field = unquote(product_field)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    field_value = product.get(product_field.lower())
    if field_value is None:
        raise HTTPException(status_code=404, detail="Field not found")
    return {product_field: field_value}
