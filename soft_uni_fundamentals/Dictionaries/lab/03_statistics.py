products = {}
while True:
    commands = input()
    if commands == "statistics":
        break
    key, value = commands.split(": ")
    value = int(value)
    if key not in products:
        products[key] = value
    else:
        products[key] += value

print("Products in stock:")
for (key, value) in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
