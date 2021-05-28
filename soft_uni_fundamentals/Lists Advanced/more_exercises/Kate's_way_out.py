def find_kate(mx):
    for i in range(len(mx)):
        for j in range(len(mx[i])):
            if mx[i][j] == 'k':
                return i, j


def kate_moves(matrix, moves, kate_pos=None, count=0):
    if kate_pos is None:
        kate_pos = []
    while True:
        position = find_kate(matrix)
        if position is None:
            if not kate_pos:
                return 'Kate cannot get out'
            else:
                return f"Kate got out in {sum([r.count('K') for r in matrix])} moves"
        else:
            r, c = position
        matrix[r][c] = 'K'
        for move in moves:
            new_r, new_c = moves[move]
            pot_row, pot_col = r + new_r, c + new_c
            if pot_row < len(matrix) and 0 <= pot_col < len(matrix[r]):
                if matrix[pot_row][pot_col] == " ":
                    count += 1
                    matrix[pot_row][pot_col] = "k"
                    kate_moves(matrix, moves, kate_pos, count)
            else:
                count += 1
                kate_pos.append(count)


moves = {
    "right": [0, 1],
    "left": [0, -1],
    "up": [-1, 0],
    "down": [1, 0],

}

matrix = [list(input()) for i in range(int(input()))]
print(kate_moves(matrix, moves))