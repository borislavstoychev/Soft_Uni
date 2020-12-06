array = list(map(int, input().split()))

while True:
    commands = input()
    if commands == "end":
        break
    if commands == "decrease":
        array = [_ - 1 for _ in array]
    command = commands.split()[0]
    if command == "swap":
        index1, index2 = commands.split()[1], commands.split()[2]
        index1 = int(index1)
        index2 = int(index2)
        num1 = array[index1]
        num2 = array[index2]
        array[index1] = num2
        array[index2] = num1
    elif command == "multiply":
        index1, index2 = commands.split()[1], commands.split()[2]
        index1 = int(index1)
        index2 = int(index2)
        number_to_insert = array[index1] * array[index2]
        array.pop(index1)
        array.insert(index1, number_to_insert)

print(", ".join(list(map(str, array))))
