def equal_square(matrix):
    result = 0
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            if i - 1 >= 0 and j - 1 >= 0:
                if matrix[i][j] == matrix[i][j - 1] and \
                        matrix[i][j] == matrix[i - 1][j] and \
                        matrix[i][j] == matrix[i - 1][j - 1]:
                    result += 1
    return result


rows, columns = list(map(int, input().split()))
matrix = [input().split() for i in range(rows)]
print(equal_square(matrix))
