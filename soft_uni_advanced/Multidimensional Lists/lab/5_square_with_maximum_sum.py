def matrix_squares(matrix):
    matrix_square = []
    for i in range(len(matrix) - 1):
        row = matrix[i]
        for j in range(len(row) - 1):
            square = [
                matrix[i][j], matrix[i][j + 1],
                matrix[i + 1][j], matrix[i + 1][j + 1]
            ]
            matrix_square.append(square)
    return matrix_square


rows, columns = list(map(int, input().split(", ")))

matrix = [(list(map(int, (input().split(", "))))) for _ in range(rows)]

max_matrix_squares = max(matrix_squares(matrix), key=lambda x: sum(x))

print(*max_matrix_squares[:len(max_matrix_squares) // 2])
print(*max_matrix_squares[len(max_matrix_squares) // 2:])
print(sum(max_matrix_squares))