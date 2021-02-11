def is_valid(num, nr, nc):
    return 0 <= nr < num and 0 <= nc < num


def moves(matrix, all_commands, commands_dict, start, sym, l):
    for com in all_commands:
        start_row, start_col = start
        new_row, new_col = commands_dict[com]
        potential_rol = start_row + new_row
        potential_col = start_col + new_col
        if is_valid(n, potential_rol, potential_col):
            if matrix[potential_rol][potential_col] == sym[0]:
                l.pop()
            elif matrix[potential_rol][potential_col] == sym[1]:
                return f"Game over! {potential_rol, potential_col}"
            matrix[start_row][start_col] = "*"
            start = (potential_rol, potential_col)
    return matrix, l, start


n = int(input())
command = input().split()
symbols = ["c", "e"]
commands = {
    "right": [0, 1],
    "left": [0, -1],
    "up": [-1, 0],
    "down": [1, 0]
}

field = [[row for row in input().split()]for _ in range(n)]
start_position = []
list_coals = []
for i in range(n):
    for j in range(n):
        if field[i][j] == "s":
            start_position = [i, j]
        elif field[i][j] == "c":
            list_coals.append("coals")
try:
    result, list_coals, last_position = moves(field, command, commands, start_position, symbols, list_coals)
    if not list_coals:
        print(f"You collected all coals! {last_position}")
    else:
        print(f"{len(list_coals)} coals left. {last_position}")
except ValueError:
    print(moves(field, command, commands, start_position, symbols, list_coals))
