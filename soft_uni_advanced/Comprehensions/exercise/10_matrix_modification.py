matrix = [[int(el) for el in input().split()] for _ in range(int(input()))]
commands = input()
while not commands == "END":
    command, row, col, value = commands.split()
    row, col, value = int(row), int(col), int(value)
    if command == "Add" and row in range(len(matrix)) and col in range(len(matrix)):
        matrix[row][col] += value
    elif command == "Subtract" and row in range(len(matrix)) and col in range(len(matrix)):
        matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    commands = input()
[print(*sublist) for sublist in matrix]