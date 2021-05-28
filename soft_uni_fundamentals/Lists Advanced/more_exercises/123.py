def get_matrix_and_position(n=int(input())):
    mat = []
    kate = []
    possible_moves = []
    for i in range(n):
        rows = list(input())
        sub_mat = []
        for j in range(len(rows)):
            sub_mat.append(rows[j])
            if rows[j] == "k":
                kate.append([i, j])
            elif rows[j] == " ":
                possible_moves.append([i, j])
        mat.append(sub_mat)
    return mat, kate, possible_moves


def kate_moves(matrix, moves, kate_pos, poss_move, all_moves=[], count=0):
    for move in moves:
        r, c = kate_pos[0]
        matrix[r][c] = 'K'
        new_r, new_c = moves[move]
        pot_row, pot_col = r + new_r, c + new_c
        if pot_row < len(matrix) and 0 <= pot_col < len(matrix[r]):
            if matrix[pot_row][pot_col] == " ":
                count += 1
                matrix[pot_row][pot_col] = "K"
                kate_pos[0] = [pot_row, pot_col]
                kate_moves(matrix, moves, kate_pos, poss_move, all_moves, count)
        else:
            count += 1
            all_moves.append(count)
    if all_moves:
        return f"Kate got out in {sum([r.count('K') for r in matrix])} moves"
    else:
        return "Kate cannot get out"


moves = {
    "right": [0, 1],
    "left": [0, -1],
    "up": [-1, 0],
    "down": [1, 0],
}

matrix, kate_position, poss_move = get_matrix_and_position()
print(kate_moves(matrix, moves, kate_position, poss_move))


