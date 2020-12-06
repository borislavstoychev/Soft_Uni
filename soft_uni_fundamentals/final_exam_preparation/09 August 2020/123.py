n = int(input())
plant_discovery = {}
for _ in range(n):
    line = input().split("<->")
    plant, rarity = line[::]
    rarity = int(rarity)
    plant_discovery[plant] = {"Rarity": rarity, "Rating": []}

commands = input()
while not commands == "Exhibition":
    command, token = commands.split(": ")[::]
    token = str(token)
    if command == "Rate":
        plant_r, rating = token.split(" - ")
        rating = int(rating)
        if plant_r in plant_discovery:
            plant_discovery[plant_r]["Rating"].append(rating)
        else:
            print("error")
    elif command == "Update":
        plant_u, new_rarity = token.split(" - ")
        if plant_u in plant_discovery:
            plant_discovery[plant_u]["Rarity"] = int(new_rarity)
        else:
            print("error")
    elif command == "Reset":
        plant_reset = token
        if plant_reset in plant_discovery:
            plant_discovery[plant_reset]["Rating"].clear()
        else:
            print("error")
    else:
        print("error")
    commands = input()

for (key, value) in plant_discovery.items():
    if not len(value["Rating"]) == 0:
        plant_discovery[key]["Rating"] = sum(plant_discovery[key]["Rating"]) / len(plant_discovery[key]["Rating"])
    else:
        plant_discovery[key]["Rating"] = 0
print("Plants for the exhibition:")
for (key, value) in dict(sorted(plant_discovery.items(), key=lambda el: (-el[1]["Rarity"], -el[1]["Rating"]))).items():
    print(f"- {key}; Rarity: {value['Rarity']}; Rating: {value['Rating']:.2f}")
