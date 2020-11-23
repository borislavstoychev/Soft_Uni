train_wagons = int(input())

wagons_list = list(0 for _ in range(train_wagons))

command = input()

while not command == "End":
    token = command.split()
    key_word = token[0]
    if key_word == "add":
        passenger = int(token[1])
        wagons_list[-1] += passenger
    elif key_word == "insert":
        wagon = int(token[1])
        passenger = int(token[2])
        wagons_list[wagon] += passenger
    elif key_word == "leave":
        wagon = int(token[1])
        passenger = int(token[2])
        wagons_list[wagon] -= passenger

    command = input()

print(wagons_list)