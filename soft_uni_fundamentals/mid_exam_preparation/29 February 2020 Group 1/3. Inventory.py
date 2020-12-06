journal = input().split(", ")

while True:
    commands = input()
    if commands == "Craft!":
        break
    command, item = commands.split(" - ")
    if command == "Collect":
        if item not in journal:
            journal.append(item)
    elif command == "Drop":
        if item in journal:
            journal.remove(item)
    elif command == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in journal:
            index = int(journal.index(old_item) + 1)
            journal.insert(index, new_item)
    elif command == "Renew":
        if item in journal:
            journal.remove(item)
            journal.append(item)


print(", ".join(journal))


