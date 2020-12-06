friends = input().split(", ")
count_blacklist = 0
count_lost = 0
while True:
    commands = input()
    if commands == "Report":
        break
    command = commands.split()[0]
    if command == "Blacklist":
        name = commands.split()[1]
        if name in friends:
            count_blacklist += 1
            print(f"{name} was blacklisted.")
            index = friends.index(name)
            friends[index] = "Blacklisted"
        else:
            print(f"{name} was not found.")
    elif command == "Error":
        index = int(commands.split()[1])
        if not friends[index] == "Blacklisted" and not friends[index] == "Lost" and index in range(len(friends)):
            print(f"{friends[index]} was lost due to an error.")
            friends[index] = "Lost"
            count_lost += 1
    elif command == "Change":
        index1 = int(commands.split()[1])
        new_name = commands.split()[2]
        if index1 in range(len(friends)):
            print(f"{friends[index1]} changed his username to {new_name}.")
            friends[index1] = new_name

print(f"Blacklisted names: {count_blacklist}")
print(f"Lost names: {count_lost}")
print(" ".join(friends))

