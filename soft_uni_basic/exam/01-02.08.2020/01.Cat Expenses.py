bad_price = float(input())
toilet_price=float(input())

cat_food = toilet_price+(toilet_price * 0.25)
toys = (cat_food * 0.5)
vet_price = toys + (toys * 0.10)
price_per_month = toilet_price + cat_food + toys + vet_price
unexpected = price_per_month * 0.05
total_price = bad_price + (12 * price_per_month) + (12 * unexpected)
print(f'{total_price:.2f} lv.')