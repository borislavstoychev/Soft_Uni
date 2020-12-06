import re

total = 0
items = []

pattern = r'>>(?P<product>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<qty>\d+)(?!.)'

furniture = input()
while not furniture == 'Purchase':
    if re.match(pattern, furniture):
        data = re.search(pattern, furniture)
        product, price, qty = data.group('product', 'price', 'qty')
        items.append(product)
        total += float(price) * int(qty)

    furniture = input()

print(f"Bought furniture:")
[print(item)for item in items]
print(f'Total money spend: {total:.2f}')
