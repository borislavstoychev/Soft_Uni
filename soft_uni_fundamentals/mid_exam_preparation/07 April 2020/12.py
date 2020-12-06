numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if index <= len(numbers) - 1:
        shooting_index = numbers[index]
        numbers.pop(index)
        count = -1
        for number in numbers:
            count += 1
            if number > shooting_index and not shooting_index == -1:
                number -= shooting_index
                numbers.pop(count)
                numbers.insert(count, number)
            else:
                if not number == -1 and not shooting_index == -1:
                    number += shooting_index
                    numbers.pop(count)
                    numbers.insert(count, number)

        numbers.insert(index, -1)

print(f"Shot targets: {len([_ for _ in numbers if _ == -1])} -> {' '.join(list(map(str, numbers)))}")

