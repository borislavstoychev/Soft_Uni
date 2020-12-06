numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if index < len(numbers):
        shooting_index = numbers[index]
        numbers.pop(index)
        for i in range(len(numbers)):
            if numbers[i] > shooting_index:
                numbers[i] -= shooting_index
            else:
                if not numbers[i] == -1:
                    numbers[i] += shooting_index

        numbers.insert(index, -1)

print(f"Shot targets: {len([_ for _ in numbers if _ == -1])} -> {' '.join(list(map(str, numbers)))}")
