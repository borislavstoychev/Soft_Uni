from collections import deque

peoples = deque()
quantity = int(input())
line = input()
while not line == "Start":
    name = line
    peoples.append(name)
    line = input()
commands = input()
while not commands == "End":
    if commands.isdigit():
        liters = int(commands)
        if liters <= quantity:
            print(f"{peoples.popleft()} got water")
            quantity -= liters
        else:
            print(f"{peoples.popleft()} must wait")
    else:
        upgrade = commands.split()[1]
        upgrade = int(upgrade)
        quantity += upgrade
    commands = input()
print(f"{quantity} liters left")
