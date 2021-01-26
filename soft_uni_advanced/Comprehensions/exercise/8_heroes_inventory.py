heroes_dict = {h: {} for h in input().split(", ")}
line = input()
while not line == "End":
    name, item, cost = line.split("-")
    cost = int(cost)
    if not heroes_dict[name].get(item):
        heroes_dict[name].update({item: cost})
    line = input()
print(*[f"{key} -> Items: {len(value)}, Cost: {sum([value[price] for price in value])}" for key, value in
        heroes_dict.items()], sep="\n")
