import requests

url = 'https://dummyjson.com/products'

params = {
    'limit': 10
}

response = requests.get(url)

# print(response.status_code)
# print(response.content)
# print(response.text)
result = response.json()
products = result['products']

total_cost = 0
total_cost_apple = 0
total_cost_premium = 0

for product in products:
    print(product)
    price = product['price']
    stock = product['stock']
    product_cost = price * stock
    total_cost += product_cost

    if product['brand'] == 'Apple':
        total_cost_apple += product_cost

    if price > 400:
        total_cost_premium += product_cost

print(f'{total_cost}')
