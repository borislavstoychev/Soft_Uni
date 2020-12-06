price = 0
# If the customer is special, then he has a 10% discount of the price of the total price with taxes.
is_baying = False
customer = ""
while True:
    line = input()
    customer = line
    if line == "special" or line == "regular":
        break
    prices = float(line)
    if prices < 0:
        print("Invalid price!")
        continue
    price += prices
    is_baying = True

taxes = price * 0.2
price_and_taxes = price + taxes
if customer == "special" and is_baying:
    price_and_taxes -= 0.1 * price_and_taxes
if is_baying:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {price:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n-----------\nTotal price: {price_and_taxes:.2f}$")
else:
    print("Invalid order!")



