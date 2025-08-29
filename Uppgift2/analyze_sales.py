import csv
import os
import locale
from collections import Counter

os.system('cls')

def format_currency(value):
    return locale.currency(value, grouping=True)

def load_sales(filename):
    products_data = {}
    all_products = []
    list_products = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = row['Product']
            sales = float(row['Sales'])
            
            list_products.append(product)
            all_products.append(product)
            
            if product in products_data:
                products_data[product] += sales
            else:
                products_data[product] = sales

    return products_data, all_products, list_products

def analyze_sales_data(products_data, all_products, list_products):
    
    product_count = Counter(all_products)
    most_common_product = product_count.most_common(1)[0]

    most_lucrative_product = max(products_data, key=products_data.get)
    product_value = products_data[most_lucrative_product]
    
    print(f"Mest sålda produkt: {most_common_product[0]}, Antal: {most_common_product[1]}")
    print(f"Mest lukrativa produkt: \"{most_lucrative_product}\" med försäljning på {format_currency(product_value)}")

try:
    locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_ALL, '')

products_data, all_products, list_products = load_sales('sales_data.csv')
analyze_sales_data(products_data, all_products, list_products)