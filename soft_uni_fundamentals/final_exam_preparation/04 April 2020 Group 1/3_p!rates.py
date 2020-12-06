line = input()
cites = {}
while not line == "Sail":
    city, population, gold = line.split("||")
    population = int(population)
    gold = int(gold)
    if city not in cites:
        cites[city] = {"Population": population, "Gold": gold}
    else:
        cites[city]["Population"] += population
        cites[city]["Gold"] += gold

    line = input()
commands = input()
while not commands == "End":
    command = commands.split("=>")[0]
    if command == "Plunder":
        town, people, gold = commands.split("=>")[1:]
        people = int(people)
        gold = int(gold)
        if town in cites:
            cites[town]["Population"] -= people
            cites[town]["Gold"] -= gold
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            if cites[town]["Population"] <= 0 or cites[town]["Gold"] <= 0:
                print(f"{town} has been wiped off the map!")
                del cites[town]
    elif command == "Prosper":
        town, gold = commands.split("=>")[1:]
        gold = int(gold)
        if gold > 0:
            cites[town]["Gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cites[town]['Gold']} gold.")
        else:
            print(f"Gold added cannot be a negative number!")
    commands = input()
print(f"Ahoy, Captain! There are {len(cites)} wealthy settlements to go to:")
for (key, value) in dict(sorted(cites.items(), key=lambda el: (-el[1]["Gold"], el[0]))).items():
    print(f"{key} -> Population: {value['Population']} citizens, Gold: {value['Gold']} kg")
