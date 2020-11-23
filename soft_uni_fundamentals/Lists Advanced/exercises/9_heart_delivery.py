houses = list(map(int, input().split("@")))

command = input()
previous_index = 0
count = 0
while not command == "Love!":
    jump, index = command.split()
    index = int(index)
    previous_index += index
    if previous_index >= len(houses):
        previous_index = 0
    houses[previous_index] -= 2
    if houses[previous_index] == 0:
        count += 1
        print(f"Place {previous_index} has Valentine's day.")
    elif houses[previous_index] < 0:
        houses[previous_index] = 0
        print(f"Place {previous_index} already had Valentine's day.")

    command = input()
print(f"Cupid's last position was {previous_index}.")
if sum(houses) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(houses) - count} places.")
