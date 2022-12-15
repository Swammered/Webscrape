import json
import csv

f = open('FoodLion.json',)
data = json.load(f)

with open('FoodLion_DATA.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    for product in data['items']:            
        product_details = [product['name'], product['base_price'], product['uom_price']['price'], product['sale_price']]

        writer.writerow(product_details)
