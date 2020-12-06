initial_list = input().split("!")

while True:
    commands = input()
    if commands == "Go Shopping!":
        break
    command = commands.split()[0]
    items1 = commands.split()[1]
    if command == "Urgent":
        if items1 not in initial_list:
            initial_list.insert(0, items1)
    elif command == "Unnecessary":
        if items1 in initial_list:
            initial_list.remove(items1)
    elif command == "Correct":
        items2 = commands.split()[2]
        if items1 in initial_list:
            index = initial_list.index(items1)
            initial_list.pop(index)
            initial_list.insert(index, items2)
    elif command == "Rearrange":
        if items1 in initial_list:
            initial_list.remove(items1)
            initial_list.append(items1)

print(', '.join(initial_list))


