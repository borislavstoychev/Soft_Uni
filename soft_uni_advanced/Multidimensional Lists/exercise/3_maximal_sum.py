rows, columns = list(map(int, input().split(" ")))

matrix = [[int(row) for row in input().split()] for _ in range(rows)]
matrix_3x3 = []
for i in range(len(matrix) - 2):
    row = matrix[i]
    for j in range(len(row) - 2):
        max_3x3 = [
            matrix[i][j], matrix[i][j + 1], matrix[i][j + 2],
            matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2],
            matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2],
        ]
        matrix_3x3.append(max_3x3)
max_matrix_3x3 = max(matrix_3x3, key=lambda x: sum(x))
beginning = 0
print(f"Sum = {sum(max_matrix_3x3)}")
for r in range(1, len(max_matrix_3x3) + 1):
    if r % 3 == 0:
        print(*max_matrix_3x3[beginning:r])
        beginning = r