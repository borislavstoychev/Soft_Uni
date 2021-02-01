def is_valid(r, c, matrix):
    return 0 <= r < len(matrix) and 0 <= c < len(matrix)


def explosion(matrix, row, col):
    bomb = matrix[row][col]
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if is_valid(i, j, matrix) and matrix[i][j] > 0:
                matrix[i][j] -= bomb
    return matrix


def exploding_matrix(booms, matrix):
    for boom in booms:
        ranges = [int(_) for _ in boom.split(",")]
        range_row_boom = ranges[0]
        range_col_boom = ranges[1]
        if matrix[range_row_boom][range_col_boom] > 0:
            explosion(matrix, range_row_boom, range_col_boom)
            matrix[range_row_boom][range_col_boom] = 0
    return matrix


def get_result(bombs, matrix):
    alive_cells = []
    for row in exploding_matrix(bombs, matrix):
        for col in row:
            if col > 0:
                alive_cells.append(col)
    return f"Alive cells: {len(alive_cells)}", f"Sum: {sum(alive_cells)}"


matrix = [[int(x) for x in input().split(' ')] for _ in range(int(input()))]
booms = input().split()

print(*get_result(booms, matrix), sep="\n")
[print(*row) for row in matrix]
