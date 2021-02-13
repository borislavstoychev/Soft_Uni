def get_matrix_and_positions(n, m):
    mat = []
    play_pos = []
    rabbits = []
    for i in range(n):
        rows = list(input())
        sub_mat = []
        for j in range(m):
            sub_mat.append(rows[j])
            if rows[j] == "B":
                rabbits.append([i, j])
            elif rows[j] == "P":
                play_pos = [i, j]
        mat.append(sub_mat)
    return mat, play_pos, rabbits


def is_valid(n, m, pot_r, pot_c):
    return 0 <= pot_r < n and 0 <= pot_c < m


def player_move(matrix, new_r, new_c, player_pos, win, loss):
    r, c = player_pos
    pot_row, pot_col = r + new_r, c + new_c
    if is_valid(row, col, pot_row, pot_col):
        if matrix[pot_row][pot_col] == "B":
            player_pos = [pot_row, pot_col]
            loss = True
        else:
            player_pos = [pot_row, pot_col]
            matrix[pot_row][pot_col] = "P"
    else:
        win = True
    matrix[r][c] = "."
    return matrix, player_pos, win, loss


def bunnies_spread(bunnie_pos, possible_moves, matrix, loss):
    new_bunnies = []
    while bunnie_pos:
        row_bunnie, col_bunnie = bunnie_pos.pop()
        for k, p in possible_moves.items():
            new_r, new_c = p
            pot_r, pot_c = row_bunnie + new_r, col_bunnie + new_c
            if is_valid(row, col, pot_r, pot_c) and not matrix[pot_r][pot_c] == "B":
                if matrix[pot_r][pot_c] == "P":
                    loss = True
                matrix[pot_r][pot_c] = "B"
                new_bunnies.append([pot_r, pot_c])
    return matrix, new_bunnies, loss


def get_moves(possible_moves, matrix, player_pos, bunnies_pos, win, loss):
    for move in input():
        new_row, new_col = possible_moves[move]
        matrix, player_pos, win, loss = player_move(matrix, new_row, new_col, player_pos, win, loss)
        matrix, bunnies_pos, loss = bunnies_spread(bunnies_pos, possible_moves, matrix, loss)
        if win or loss:
            return matrix, player_pos, win


def print_result(matrix, p_p, win):
    print(*["".join(f) for f in matrix], sep="\n")
    print("won: ", end="") if win else print("dead: ", end="")
    print(*p_p, sep=" ")


row, col = [int(num) for num in input().split()]
field, player_position, bunnies_positions = get_matrix_and_positions(row, col)
is_win = None
is_loss = None
moves = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}
result = get_moves(moves, field, player_position, bunnies_positions, is_win, is_loss)
print_result(*result)

