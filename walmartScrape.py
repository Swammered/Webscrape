import json
import logging
import csv

f = open('walmart.json',)
data = json.load(f)
#header = ['Product Name', ' Product Price', ' Product Price per x', 'Product Price per unit']

with open('Walmart_DATA.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    for product in data['data']['search']['searchResult']['itemStacks'][0]['itemsV2']:
        if(product['__typename'] == 'Product'):
            product_name = product['name']
            product_price = product['priceInfo']['currentPrice']['priceString']

            try:
                split_list = product['priceInfo']['unitPrice']['priceString'].split('/')
                product_price_per = split_list[0]
                product_price_per_unit = split_list[1]
            except Exception:
                logging.warning("Theres no unit price or priceString at: " + product['name'])
            
            product_details = [product_name, product_price, product_price_per, product_price_per_unit]
            writer.writerow(product_details)