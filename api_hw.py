import requests

url = 'https://dummyjson.com/products?limit=200'
response = requests.get(url)
items = response.json()

products = items.get('products', [])

for product in products:
    if 'brand' in product and product['brand'] == 'TechGear':
      print('Id brand product -', product['id'])

url_picture = 'https://cdn.dummyjson.com/products/images/smartphones/Vivo%20V9/1.png'
response = requests.get(url_picture)
with open('phone.png', mode='wb') as file:
    file.write(response.content)

total_price = []

for product in products:
    if product['price'] > 800:
        premium_products = product['price'] * product['stock']
        # print(premium_products) Залишив для перевірки результату
        total_price.append(premium_products)
total_sum = sum(total_price)
print('Total sum of premium products-', total_sum)
