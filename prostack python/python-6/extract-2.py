#extract data from rest api

import requests,json,csv

product_response = requests.get("https://dummyjson.com/products")
products = product_response.json()
print(type(products))
products_list = products['products']
print(type(products_list))

#transform data into JSON and CSV formats   

products = product_response.json()['products']

beauty_products_json = []
for product in product:
    if product['category']=='beauty':
                                                                    
