rows, columns = list(map(int, input().split(" ")))

matrix = [input().split() for _ in range(rows)]

line = input()
while not line == "END":
    try:
        swap, row1, col1, row2, col2 = line.split()
        row1 = int(row1)
        col1 = int(col1)
        row2 = int(row2)
        col2 = int(col2)
        if swap == "swap" and row1 in range(len(matrix)) and col1 in range(len(matrix)) and row2 in range(len(matrix)) and col2 in range(len(matrix)):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            print('\n'.join([" ".join(m) for m in matrix]))
        else:
            print("Invalid input!")
    except ValueError:
        print("Invalid input!")

    line = input()
