# coffee - 1.50
# water - 1.00
# coke - 1.40
# snacks - 2.00
def total_price(product, quantity):
    price = 0
    if product == "coffee":
        price = quantity * 1.50
    elif product == "water":
        price = quantity * 1
    elif product == "coke":
        price = quantity * 1.40
    elif product == "snacks":
        price = quantity * 2
    return price


chill = input()
nums = int(input())

print(f'{total_price(chill, nums):.2f}')
