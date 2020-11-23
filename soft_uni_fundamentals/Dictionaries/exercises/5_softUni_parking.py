parking = {}
for _ in range(int(input())):
    commands = input().split()
    command = commands[0]
    if command == "register":
        username = commands[1]
        car_number = commands[2]
        if username not in parking:
            parking[username] = car_number
            print(f"{username} registered {parking[username]} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[username]}")
    elif command == "unregister":
        username_to_unregistered = commands[1]
        if username_to_unregistered in parking:
            print(f"{username_to_unregistered} unregistered successfully")
            parking.pop(username_to_unregistered)
        else:
            print(f"ERROR: user {username_to_unregistered} not found")
for (key, value) in parking.items():
    print(f"{key} => {value}")