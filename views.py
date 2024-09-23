import json
from urllib.parse import unquote
from flask import Flask, jsonify, abort
from typing import List, Dict, Optional
from main import name_js_file

app = Flask(__name__)

name_js_file: str = name_js_file


def load_products_from_file(file_path: str) -> List[Dict[str, str]]:
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_path}.")
        return []


products: List[Dict[str, str]] = load_products_from_file(name_js_file)


def find_product_by_name(product_name: str) -> Optional[Dict[str, str]]:
    for product in products:
        if product['name'].lower() == product_name.lower():
            return product
    return None


@app.route("/all_products/", methods=['GET'])
def get_all_products() -> jsonify:
    if not products:
        abort(404, description="No products found")
    return jsonify(products)


@app.route("/products/<product_name>", methods=['GET'])
def get_product(product_name: str) -> jsonify:
    product_name = unquote(product_name)
    product = find_product_by_name(product_name)
    if product is None:
        abort(404, description="Product not found")
    return jsonify(product)


@app.route("/products/<product_name>/<product_field>", methods=['GET'])
def get_product_field(product_name: str, product_field: str) -> jsonify:
    product_name = unquote(product_name)
    product = find_product_by_name(product_name)
    product_field = unquote(product_field)

    if product is None:
        abort(404, description="Product not found")

    field_value = product.get(product_field.lower())
    if field_value is None:
        abort(404, description="Field not found")
    return jsonify({product_field: field_value})
