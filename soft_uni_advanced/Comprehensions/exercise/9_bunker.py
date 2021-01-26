bunker = {h: {} for h in input().split(", ")}
total_items = 0
total_quality = 0
for _ in range(int(input())):
    category, item_name, q = input().split(" - ")
    quantity, quality = q.split(";")
    quality = int(quality.split(":")[1])
    quantity = int(quantity.split(":")[1])
    if not bunker[category].get("item"):
        total_items += quantity
        total_quality += quality
        bunker[category][item_name] = {"quantity": quantity, "quality": quality}
print(f"Count of items: {total_items}")
print(f"Average quality: {total_quality / len(bunker):.2f}")
print(*[f"{key} -> {', '.join([k for k, v in value.items()])}"for key, value in bunker.items()], sep="\n")

