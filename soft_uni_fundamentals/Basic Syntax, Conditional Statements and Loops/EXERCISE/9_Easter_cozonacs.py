budget = float(input())
price_per_kg_flour: float = float(input())

price_for_pack_of_egs = 0.75 * price_per_kg_flour
price_for_liter_milk = price_per_kg_flour * 1.25
price_for_250ml_milk = price_for_liter_milk / 4
price_for_one_cozonac = price_for_pack_of_egs + price_per_kg_flour + price_for_250ml_milk
current_cozonacs_count = 0
colored_egs = 0

while budget >= price_for_one_cozonac:
    current_cozonacs_count += 1
    colored_egs += 3
    budget -= price_for_one_cozonac
    if current_cozonacs_count % 3 == 0:
        colored_egs -= current_cozonacs_count - 2
print(f'You made {current_cozonacs_count} cozonacs! Now you have {colored_egs} eggs and {budget:.2f}BGN left.')
