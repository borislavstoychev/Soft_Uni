legendary_items = {"fragments": 0, "shards": 0, "motes": 0}
legendary = {"fragments": "Valanyr", "shards": "Shadowmourne", "motes": "Dragonwrath"}
junket_items = {}
is_winner = False
winner = ""
while True:
    if is_winner:
        print(f"{legendary[winner]} obtained!")
        for (key, value) in dict(sorted(legendary_items.items(), key=lambda el: (-el[1], el[0]))).items():
            print(f"{key}: {value}")
        for (key, value) in dict(sorted(junket_items.items())).items():
            print(f"{key}: {value}")
        exit()
    elements = input().lower().split()
    for index in range(0, len(elements), 2):
        value = int(elements[index])
        item = elements[index + 1]
        if item in legendary_items:
            legendary_items[item] += value
            if legendary_items[item] >= 250:
                winner = item
                legendary_items[item] -= 250
                is_winner = True
                break
        else:
            if item not in junket_items:
                junket_items[item] = value
            else:
                junket_items[item] += value
