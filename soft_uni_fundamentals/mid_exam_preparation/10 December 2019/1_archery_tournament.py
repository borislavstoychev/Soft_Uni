numbers = list(map(int, input().split("|")))
count_points = 0
while True:
    commands = input()
    if commands == "Game over":
        break
    command = commands.split()[0]
    if command == "Shoot":
        left_or_right = commands.split()[1]
        left_right, index1, length = left_or_right.split("@")
        index1 = int(index1)
        length = int(length)
        if left_right == "Left" and 0 <= index1 < len(numbers):
            shoot = (index1 - length) % len(numbers)
            numbers[shoot] -= 5
            if numbers[shoot] < 0:
                points = numbers[shoot] + 5
                numbers[shoot] = 0
            else:
                points = 5
            count_points += points
        elif left_right == "Right" and 0 <= index1 < len(numbers):
            shoot = (index1 + length) % len(numbers)
            numbers[shoot] -= 5
            if numbers[shoot] < 0:
                points = numbers[shoot] + 5
                numbers[shoot] = 0
            else:
                points = 5
            count_points += points
    elif command == "Reverse":
        numbers = numbers[:: -1]

print(" - ".join(list(map(str, numbers))))
print(f"Iskren finished the archery tournament with {count_points} points!")