line = input()
commands = input()
while not commands == "Generate":
    command = commands.split(">>>")[0]
    if command == "Contains":
        substring = commands.split(">>>")[1]
        if substring in line:
            print(f"{line} contains {substring}")
        else:
            print(f"Substring not found!")
    elif command == "Flip":
        upper_lower, start_index, end_index = commands.split(">>>")[1:]
        start_index = int(start_index)
        end_index = int(end_index)
        if upper_lower == "Upper":
            line = line[:start_index] + line[start_index:end_index].upper() + line[end_index:]
        elif upper_lower == "Lower":
            line = line[:start_index] + line[start_index:end_index].lower() + line[end_index:]
        print(line)
    elif command == "Slice":
        start_index, end_index = commands.split(">>>")[1:]
        start_index = int(start_index)
        end_index = int(end_index)
        line = line[:start_index] + line[end_index:]
        print(line)

    commands = input()
print(f"Your activation key is: {line}")