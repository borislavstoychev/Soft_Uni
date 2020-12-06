stops = input()
line = input()
while not line == "Travel":
    command, token1, token2 = line.split(":")[::]
    if command == "Add Stop":
        index = int(token1)
        string = token2
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index:]
        print(stops)
    elif command == "Remove Stop":
        start_index = int(token1)
        stop_index = int(token2)
        if stop_index <= len(stops) > stop_index:
            stops = stops[:start_index] + stops[stop_index + 1:]
        print(stops)
    elif command == "Switch":
        old_string, new_string = token1, token2
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)

    line = input()
print(f"Ready for world tour! Planned stops: {stops}")
