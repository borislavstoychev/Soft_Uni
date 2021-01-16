def search_index(matrix, el):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == el:
                return i, j
    return f"{el} does not occur in the matrix"


matrix = [list(input()) for _ in range(int(input()))]
element = input()
print(search_index(matrix, element))
