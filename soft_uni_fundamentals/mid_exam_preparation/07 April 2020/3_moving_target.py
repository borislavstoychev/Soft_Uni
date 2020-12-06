targets = list(map(int, input().split()))

while True:
    commands = input()
    if commands == "End":
        break
    command, index, power = commands.split()
    index = int(index)
    power = int(power)
    if command == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif command == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, power)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        if index - power >= 0 and index + power < len(targets):
            targets_left = targets[:index - power]
            targets_right = targets[index + power + 1:]
            targets = targets_left + targets_right
        else:
            print("Strike missed!")

print("|".join(list(map(str, targets))))
